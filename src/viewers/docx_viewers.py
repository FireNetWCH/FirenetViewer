from PySide6.QtWidgets import QTextBrowser
from src.viewers.explorer_function import view_cleaer, MetaDataTableWiget
import mammoth
class DocxViewers (QTextBrowser):
    def __init__(self,parent = None):
        super().__init__()


def display_docx_content(context,docx_path):
    docx_viewers = DocxViewers()
    layout = context.ui.reportsPage.layout()
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        docx_viewers.setHtml(result.value)
    meta_data_system_file = MetaDataTableWiget(docx_path)
    view_cleaer(layout,context)
    layoutRP = context.ui.rightMenu.layout()
    layoutRP.addWidget(meta_data_system_file)
    layout.addWidget(docx_viewers)


