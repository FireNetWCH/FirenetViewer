from src.viewers.img_viewer import display_img_content
from src.viewers.table_viewers import display_table_content
from src.viewers.pdf_viewer import display_pdf_content
from src.viewers.txt_viewers import display_txt_content
from src.viewers.not_support_file import NotSupportFileView
def generator_wiget(file,ext):
    '''Obraz -> file is pixmap
       Arkusz kalkulacyjny -> file is dataFrama(pandas)
       PDF ->file is fitz.document
       txt ->file is string
    '''   
    if ext in ['.jpg','.jpeg','.png','.gif','.bmp','.ppm']:
        return display_img_content(file)
    elif ext in ['.csv','.xlsx','.xls','.odf','.ods','.xlsm','.xlsb']:
        return display_table_content(file)
    elif ext == '.pdf':
        return display_pdf_content(file)
    elif ext == '.txt':
        return display_txt_content(file)
    else:
        return NotSupportFileView()