from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table, TableStyle,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
import src.db_function.db_email_function as db_email
from PySide6.QtCore import QObject, QThread, Signal, Slot,Qt
import re
import os
from PySide6.QtWidgets import QFileDialog,QMessageBox
import logging
import shutil 
import pandas as pd
import math
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class pdf_worker(QObject):
    finish = Signal()
    message = Signal(str)
    progres_stats = Signal(int,int)
    def __init__(self, data,dir_path,attachments_options,path,sql_name):
        super().__init__()
        self.data = data
        self.dir_path = dir_path
        self.attachments_options = attachments_options
        self.path = path
        self.sql_name = sql_name

    def run(self):
        
        if self.data:
            first_row = self.data[0]
            num_columns = len(first_row)
            if num_columns == 9:
                self.data = [row[:-2] for row in self.data]
        df = pd.DataFrame(self.data, columns=["Id", "Data", "Nadawca", "Odbiorca", "Temat","Treść", "Załączniki"])
        
        self.dir_path = os.path.join(self.dir_path,self.sql_name)
        count = 1
        checked_path = self.dir_path
        while os.path.exists(checked_path):
            checked_path = self.dir_path + f"({count})"
            count = count + 1
        os.mkdir(checked_path)
        self.dir_path = checked_path

        #file_path = file_path.removesuffix(os.path.dirname(dir_path))
        all_doc = len(df)
        
        count_exported = 1
        for index, row in df.iterrows():
            if row["Temat"] is not None:
                subject_to_path = re.sub(r'[?/*<>|\\:",.\s]','_',row["Temat"])
                subject_to_path = subject_to_path[:50]
            else:
                subject_to_path = "BRAK_TEMATU"
            if (row["Załączniki"] is not None) and self.attachments_options:
                try:   
                    shutil.copytree(os.path.join(self.path,self.sql_name,"Attachments",str(row["Id"])),os.path.join(self.dir_path,"ID_"+str(row["Id"])+"_"+subject_to_path+"_Załączniki_wiadomości"))
                except:
                    logger.error(f"brak zołączników we wskazanym miejscu: {os.path.join(self.path,self.sql_name,"Attachments",str(row["Id"]))}")
            pdf_path = os.path.join(self.dir_path,"ID_"+str(row["Id"])+'_'+subject_to_path) +".pdf"
            try:
                generate_pdf(pdf_path,row["Nadawca"],row["Odbiorca"],row["Data"],row["Temat"],row["Załączniki"],row["Treść"],row["Id"],self.sql_name,False)
            except:
                generate_pdf(pdf_path,row["Nadawca"],row["Odbiorca"],row["Data"],row["Temat"],row["Załączniki"],row["Treść"],row["Id"],self.sql_name,True)
            self.progres_stats.emit(all_doc,count_exported)
            count_exported = count_exported + 1 
        logger.info(f"Plik PDF zapisany jako: {self.dir_path}")
        self.message.emit("Export zostało zakończony")
        
        self.finish.emit()

class exel_worker(QObject):
    finish = Signal()
    message = Signal(str)
    progres_stats = Signal(int,int)
    def __init__(self, data,dir_path,attachments_options,path,sql_name,file_path):
        super().__init__()
        self.data = data
        self.dir_path = dir_path
        self.attachments_options = attachments_options
        self.path = path
        self.sql_name = sql_name
        self.file_path = file_path

    def run(self):
        
        modified_data = []
        for row in self.data:
            row_list = list(row)
            if row_list[5] is not None:
                row_list[5] = remove_multi_new_line(row_list[5])
                row_list[5].replace("<br>","")
            modified_data.append(tuple(row_list))
        self.dir_path = self.file_path
    
        self.dir_path = os.path.join(self.dir_path,self.sql_name)
        count = 1
        checked_path = self.dir_path
        while os.path.exists(checked_path):
            checked_path = self.dir_path + f"({count})"
            count = count + 1
        os.mkdir(checked_path)
        self.dir_path = checked_path



        os.mkdir(os.path.join(self.dir_path,"Attachments"))
        df = pd.DataFrame(modified_data, columns=["Id", "Data", "Nadawca", "Odbiorca", "Temat","Treść", "Załączniki"])

        all_doc = len(df)
        
        count_exported = 1
        for index, row in df.iterrows():
            if row["Załączniki"] is not None and self.attachments_options:
                subject_to_path = re.sub(r'[?/*<>|\\:",.\s]','_',row["Temat"])
                subject_to_path = subject_to_path[:50]
                try:
                    shutil.copytree(os.path.join(self.path,self.sql_name,"Attachments",str(row["Id"])),os.path.join(self.dir_path,"Attachments","ID_"+str(row["Id"])+"_"+subject_to_path+"_Załączniki_wiadomości"))
                except:
                    logger.error(f"brak zołączników we wskazanym miejscu{os.path.join(self.path,self.sql_name,"Attachments",str(row["Id"]))}")
            self.progres_stats.emit(all_doc,count_exported)
            count_exported = count_exported + 1
        with pd.ExcelWriter(os.path.join(self.dir_path,self.sql_name+".xlsx"), engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Wiadomości", index=False)
            workbook = writer.book
            worksheet = writer.sheets["Wiadomości"]
            wrap_format = workbook.add_format({'text_wrap': True, 'align': 'left', 'valign': 'top'})

            worksheet.set_column("E:E", 40, wrap_format) 
            worksheet.set_column("F:F", 60, wrap_format)  
            worksheet.set_column("G:G", 50, wrap_format)
            

            row_offset = 1  

            i = 0
            while i < len(df):
                text_length = len(str(df.loc[i, "Treść"]))
                if text_length > 900:
                    num_rows = math.ceil(text_length / 900)
                    extr_chars = text_length - 900 * (num_rows-1)
                    calculated_height = (extr_chars / 45) * 13
                    worksheet.merge_range(row_offset, 0, row_offset + num_rows-1, 0, df.loc[i, "Id"], wrap_format)
                    worksheet.merge_range(row_offset, 1, row_offset + num_rows-1, 1, df.loc[i, "Data"], wrap_format)
                    worksheet.merge_range(row_offset, 2, row_offset + num_rows-1, 2, df.loc[i, "Nadawca"], wrap_format)
                    worksheet.merge_range(row_offset, 3, row_offset + num_rows-1, 3, df.loc[i, "Odbiorca"], wrap_format)
                    worksheet.merge_range(row_offset, 4, row_offset + num_rows-1, 4, df.loc[i, "Temat"], wrap_format)
                    worksheet.merge_range(row_offset, 5, row_offset + num_rows-1, 5, df.loc[i, "Treść"], wrap_format)
                    worksheet.merge_range(row_offset, 6, row_offset + num_rows-1, 6, df.loc[i, "Załączniki"], wrap_format)

                    for j in range(num_rows - 1):
                        worksheet.set_row(row_offset + j, 407)
                    worksheet.set_row(row_offset + num_rows - 1, calculated_height) 
                    
                    row_offset += num_rows
                else:
                    row_offset += 1  
                i += 1
                worksheet.set_row(row_offset, None)

        self.message.emit("Export zostało zakończony")
        self.finish.emit()

def generate_pdf(output_path, sender, receiver, date, subject, attachments, body,id_email,name_email_box,soft_text):
    """Eksportuje pojedynczą wiadomość email jako plik PDF z obsługą podziału na strony."""
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSansCondensed.ttf'))
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    

    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        name='CustomStyle',
        parent=styles['Normal'],
        fontName='DejaVu',
        fontSize=12,
        spaceAfter=12
    )
    def wrap_text(text):
        return Paragraph(text, custom_style)
    if attachments is None:
        attachments =""
    if sender is None:
        sender =""
    if receiver is None:
        receiver =""
    if date is None:
        date =""
    if body is None:
        body =""
    if subject is None:
        subject =""
    data = [
        ["Parametr:", "Wartość:"],
        ["Nadawca:", wrap_text(sender)],
        ["Odbiorca:", wrap_text(receiver)],
        ["Data:", wrap_text(date)],
        ["Temat:", wrap_text(subject)],
        ["Lista załączników:", wrap_text(attachments)]
    ]
    
   
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVu'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    
    table = Table(data, colWidths=[120, doc.width - 120])
    table.setStyle(table_style)
    #print(body)
    tekst = body
    #print(tekst)
    tekst_html = tekst.replace('<br>', '<br/>')
    tekst_html = tekst_html.replace('\n', '<br/>')
    tekst_html = re.sub(r'<img[^>]*>', '', tekst_html) 
    soup = BeautifulSoup(tekst_html, 'html.parser')
    for tag in soup.find_all(True):
        if tag.has_attr('style'):
            del tag['style']
        if tag.has_attr('class'):
            del tag['class']
    if soft_text == True:
        for span_tag in soup.find_all(['span','a','br']):
            span_tag.unwrap()
    else:
        for span_tag in soup.find_all(['span','a']):
            span_tag.unwrap()
    for tag in soup.find_all(['span', 'style', 'script', 'head','font','a']):
        tag.decompose()
    heder = f"Wiadomość wyeksportowana ze skrzynki e-mail:{name_email_box} o ID:{id_email}"
    header_paragraph = Paragraph(heder, custom_style)
    body_paragraph = Paragraph(str(soup), custom_style)
    elements = [header_paragraph,table, body_paragraph]
    doc.build(elements)
    

def remove_multi_new_line(text):
    # text = text.decode('utf-8')
    text = re.sub(r'(\r?\n)+', '\n', text)
    text = re.sub(r'(\r?\n)+', '\n', text)  
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'(\s*\n\s*)+', '\n', text)
    text = re.sub(r'<br\s*/?>', '', text)
    text = re.sub(r'<img[^>]*>', '', text) 
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup.find_all(True):
        if tag.has_attr('style'):
            del tag['style']
        if tag.has_attr('class'):
            del tag['class']
    for span_tag in soup.find_all(['span','p','td','tr','div','a','body','html','strong','tbody','table']):
        span_tag.unwrap()
    for tag in soup.find_all(['span', 'style', 'script', 'head','font','hr']):
        tag.decompose()   
    
    return str(soup)


def export_to_pdf(self,db_connection,path,sql_name,active_filters,emeils_grout,attachments_options) -> None:
        """Eksportuje emaile oznaczone flagami do pliku PDF."""
        dir_path = QFileDialog.getExistingDirectory(self.main, "Wybierz folder do zapisu PDF")
        if not dir_path:
            return
        if emeils_grout == "1":
            data = db_email.emails_to_export(db_connection)
        elif emeils_grout == "2":
            data = db_email.emails_to_export(db_connection,active_filters)
        else:
            selected_indexes = self.ui.tableWidget.selectedIndexes()
            selected_rows = set(index.row() for index in selected_indexes)
            id_list=[]
            for row in selected_rows:
                id_list.append(self.ui.tableWidget.item(row,0).text())

            data = db_email.emails_to_export(db_connection,list=id_list)
        self.ui.progressBar.setMaximum(len(data))
        self.ui.widget_42.show()
        self.ui.progressBar.show()
        self.thread = QThread()
        self.worker = pdf_worker(data,dir_path,attachments_options,path,sql_name)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finish.connect(self.thread.quit)
        self.worker.finish.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.message.connect(self.date_wornig,type=Qt.QueuedConnection)
        self.worker.progres_stats.connect(self.export_progrs)
        self.thread.start()

def export_to_excel(self,db_connection,path,sql_name,active_filters,emeils_grout,attachments_options) -> None:
        """Eksportuje dane oznaczone flagami do tabeli"""
        file_path = QFileDialog.getExistingDirectory(self.main, "Wybierz folder do zapisu Exela")
        if not file_path:
            return
        
        if emeils_grout == "1":
            data = db_email.emails_to_export(db_connection)
        elif emeils_grout == "2":
            data = db_email.emails_to_export(db_connection,active_filters)
        else:
            selected_indexes = self.ui.tableWidget.selectedIndexes()
            selected_rows = set(index.row() for index in selected_indexes)
            id_list=[]
            for row in selected_rows:
                id_list.append(self.ui.tableWidget.item(row,0).text())
            data = db_email.emails_to_export(db_connection,list=id_list)
        self.ui.progressBar.setMaximum(len(data))
        self.ui.widget_42.show()
        self.ui.progressBar.show()
        self.thread = QThread()
        self.worker = exel_worker(data,file_path,attachments_options,path,sql_name,file_path)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finish.connect(self.thread.quit)
        self.worker.finish.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progres_stats.connect(self.export_progrs)
        self.worker.message.connect(self.date_wornig,type=Qt.QueuedConnection)
        self.thread.start()
        # modified_data = []
        # for row in data:
        #     row_list = list(row) 
        #     row_list[5] = remove_multi_new_line(row_list[5])
        #     row_list[5].replace("<br>","")
        #     modified_data.append(tuple(row_list))
        # dir_path = file_path
    
        # dir_path = os.path.join(dir_path,self.sql_name)
        # os.mkdir(dir_path)
        # os.mkdir(os.path.join(dir_path,"Attachments"))
        # df = pd.DataFrame(modified_data, columns=["Id", "Data", "Nadawca", "Odbiorca", "Temat","Treść", "Załączniki"])
        # for index, row in df.iterrows():
        #     if row["Załączniki"] is not None and attachments_options:
        #         subject_to_path = re.sub(r'[?/*<>|\\:",.\s]','_',row["Temat"])
        #         subject_to_path = subject_to_path[:50]
        #         shutil.copytree(os.path.join(path,sql_name,"Attachments",str(row["Id"])),os.path.join(dir_path,"Attachments","ID_"+str(row["Id"])+"_"+subject_to_path+"_Załączniki_wiadomości"))
            
        # with pd.ExcelWriter(os.path.join(dir_path,self.sql_name+".xlsx"), engine="xlsxwriter") as writer:
        #     df.to_excel(writer, sheet_name="Wiadomości", index=False)
        #     workbook = writer.book
        #     worksheet = writer.sheets["Wiadomości"]
        #     wrap_format = workbook.add_format({'text_wrap': True, 'align': 'left', 'valign': 'top'})

        #     worksheet.set_column("E:E", 40, wrap_format) 
        #     worksheet.set_column("F:F", 60, wrap_format)  
        #     worksheet.set_column("G:G", 50, wrap_format)
            

        #     row_offset = 1  

        #     i = 0
        #     while i < len(df):
        #         text_length = len(str(df.loc[i, "Treść"]))
        #         if text_length > 900:
        #             num_rows = math.ceil(text_length / 900)
        #             extr_chars = text_length - 900 * (num_rows-1)
        #             calculated_height = (extr_chars / 45) * 13
        #             worksheet.merge_range(row_offset, 0, row_offset + num_rows-1, 0, df.loc[i, "Id"], wrap_format)
        #             worksheet.merge_range(row_offset, 1, row_offset + num_rows-1, 1, df.loc[i, "Data"], wrap_format)
        #             worksheet.merge_range(row_offset, 2, row_offset + num_rows-1, 2, df.loc[i, "Nadawca"], wrap_format)
        #             worksheet.merge_range(row_offset, 3, row_offset + num_rows-1, 3, df.loc[i, "Odbiorca"], wrap_format)
        #             worksheet.merge_range(row_offset, 4, row_offset + num_rows-1, 4, df.loc[i, "Temat"], wrap_format)
        #             worksheet.merge_range(row_offset, 5, row_offset + num_rows-1, 5, df.loc[i, "Treść"], wrap_format)
        #             worksheet.merge_range(row_offset, 6, row_offset + num_rows-1, 6, df.loc[i, "Załączniki"], wrap_format)

        #             for j in range(num_rows - 1):
        #                 worksheet.set_row(row_offset + j, 407)
        #             worksheet.set_row(row_offset + num_rows - 1, calculated_height) 
                    
        #             row_offset += num_rows
        #         else:
        #             row_offset += 1  
        #         i += 1
        #         worksheet.set_row(row_offset, None)
            
        logger.info(f"Plik Excel zapisany jako: {file_path}")