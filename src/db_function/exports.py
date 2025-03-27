from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table, TableStyle,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
import re
def generate_pdf(output_path, sender, receiver, date, subject, attachments, body,id_email,name_email_box):
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
    tekst = body.decode("utf-8")
    tekst_html = tekst.replace('\n', '<br/>')
    heder = f"Wiadomość wyeksportowana ze skrzynki e-mail:{name_email_box} o ID:{id_email}"
    header_paragraph = Paragraph(heder, custom_style)
    body_paragraph = Paragraph(tekst_html, custom_style)
    elements = [header_paragraph,table, body_paragraph]
    doc.build(elements)
    

def remove_multi_new_line(text):
    text = text.decode('utf-8')
    text = re.sub(r'(\r?\n)+', '\n', text)
    text = re.sub(r'(\r?\n)+', '\n', text)  
    text = re.sub(r'\n{2,}', '\n', text)
    text = re.sub(r'(\s*\n\s*)+', '\n', text)    
    return text
