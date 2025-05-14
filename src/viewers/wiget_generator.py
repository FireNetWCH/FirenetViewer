from src.viewers.img_viewer import display_img_content
from src.viewers.table_viewers import display_table_content
from src.viewers.pdf_viewer import display_pdf_content
from src.viewers.txt_viewers import display_txt_content
from src.viewers.docx_viewers import display_docx_content
from src.viewers.video_viewer import display_vidoe_content
from src.viewers.not_support_file import NotSupportFileView
def generator_wiget(file,ext,name = None,widget = None):
    '''Obraz -> file is pixmap
       Arkusz kalkulacyjny -> file is dataFrama(pandas)
       PDF ->file is fitz.document
       txt ->file is string
       docx-> path to file(przerobić na stromien bytes)
       vide/audio-> path to file(przerobić na stromien bytes)
    '''   
    if ext in ['jpg','jpeg','png','gif','bmp','ppm']:
        return display_img_content(file,widget)
    elif ext in ['csv','xlsx','xls','odf','ods','xlsm','xlsb']:
        return display_table_content(file)
    elif ext == 'pdf':
        return display_pdf_content(file,parent_wiget=widget)
    elif ext == 'txt':
        return display_txt_content(file)
    elif ext == 'docx':
        return display_docx_content(file)
    elif ext =='mp4':
        return display_vidoe_content(file)
    else:
        return NotSupportFileView(file,name,ext)