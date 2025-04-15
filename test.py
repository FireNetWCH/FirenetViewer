# import sqlite3


# conn = sqlite3.connect("D:\\SQL_and_header\\jsaganowska\\jsaganowska.sqlite")
# cursor = conn.cursor()
# cursor.execute('SELECT sqlite_version();')
# version = cursor.fetchone()
# print(f"SQLite Version: {version[0]}")
# # conn.text_factory = str
# cursor = conn.cursor()

# query = '''
#     SELECT e.id, e.sender_name, e.cc, e.subject, e.date, e.flag,
#                    GROUP_CONCAT(t.tag_name) AS tags
#             FROM emails e
#             LEFT JOIN email_tags et ON e.id = et.email_id
#             LEFT JOIN tags t ON et.tag_id = t.id
            
#             GROUP BY e.id
# 			      HAVING t.tag_name in ('Test','Test3')
#             LIMIT 500 OFFSET 0
# '''
# # cursor.execute("SELECT body FROM emails LIMIT 5")
# cursor.execute(query,)
# data = cursor.fetchall()

# print(f"Liczba wierszy: {len(data)}")  
# print(data[:5])  

# conn.close()

# from PyInstaller.utils.hooks import collect_submodules
# collect_submodules('lxml')

# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='main',
# )
# super().__init__(parent)
#         self.file_name = filename
#         self.file_path = file_path
#         layout = QHBoxLayout(self)
#         self.frame = QFrame()
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setLineWidth(2)
#         self.frame.setMidLineWidth(0)
#         self.frame.setFrameShadow(QFrame.Sunken)
#         self.frame.setContentsMargins(1, 1, 1, 1)
#         frame_layout = QHBoxLayout(self.frame)
#         frame_layout.setContentsMargins(1, 1, 1, 1)
#         frame_layout.setSpacing(1)
#         self.label = QLabel(filename)
#         self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         self.preview_button = QPushButton(QIcon("./Qss/icons/black/feather/link.png"), "")
#         self.preview_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         self.preview_button.clicked.connect(self.preview_file)
#         frame_layout.addWidget(self.label)
#         frame_layout.addWidget(self.preview_button)
#         frame_layout.addStretch()
#         layout.addWidget(self.frame)
#         self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         self.setContentsMargins(1, 5, 1, 5)



# 	"QPushButton": [
# 		{
# 		"name": "show_flags_btn",

#       "fallBackStyle": [
#         "background-color: #ff0000;"
#       ],
#       "defaultStyle": [
#         "background-color: #ff0000;",
# 		"hover::{background-color: #0000ff;}"
#       ]
# 		}
# 	  ]
# QCSS
# QMainWindow #tableWidget{
#     background-color: #ff0000;
#     background:#ff0000;
#     color: #00ff00;
#     ::item{
#         background-color: #ff0000
#     }
# }

# #serchEmailFrame{
#             background-color: $COLOR_ACCENT_3;
#        }

# SELECT e.id, e.sender_name, e.cc, e.subject, e.date, e.flag,
#                    GROUP_CONCAT(t.tag_name) AS tags
#             FROM emails e
#             LEFT JOIN email_tags et ON e.id = et.email_id
#             LEFT JOIN tags t ON et.tag_id = t.id

#             GROUP BY e.id
#             HAVING t.tag_name in ('2','1')
#             LIMIT 500 OFFSET 0

# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.lib import colors
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import Paragraph,Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
# def generate_pdf(output_filename, sender, receiver, date, subject, attachments):
#     c = canvas.Canvas(output_filename, pagesize=A4)
#     width, height = A4
#     margin = 50
#     y_position = height - margin
#     max_width = width - 2 * margin
#     pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSansCondensed.ttf'))
#     c.setFont("DejaVu", 12)
#     styles = getSampleStyleSheet()
#     custom_style = ParagraphStyle(
#         name='CustomStyle',
#         fontName='DejaVu',
#         fontSize=12
#     )

#     def wrap_text(text):
#         return Paragraph(text, custom_style)
    
#     texts = [["Parametr:","Wartość:"],
#             ["Nadawca:", wrap_text(sender)],
#             ["Odbiorca:", wrap_text(receiver)],
#             ["Data:", wrap_text(date)],
#             ["Temat:", wrap_text(subject)],
#             ["Lista załączników:", wrap_text(attachments)]]
             
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
#         ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#         ('FONTNAME', (0, 0), (-1, -1), 'DejaVu'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ])
#     title = "Informacje o wiadomości:"
#     c.drawString(margin, y_position, title)

#     t=Table(texts,colWidths=[120, max_width - 120])
#     t.setStyle(style)
#     table_width, table_height = t.wrap(0, 0)
#     t.wrapOn(c, width, height)
#     t.drawOn(c, margin, y_position -table_height - 20)
    
#     text_below_table = "Treść Wiadomości : "
#     text_position_y = y_position - table_height - 45
#     c.drawString(margin, text_position_y, text_below_table)

#     c.save()
#     print(f"PDF zapisano jako: {output_filename}")

# generate_pdf("output.pdf", 
#              sender="Jan Kowalski", 
#              receiver="Anna Nowak", 
#              date="2025-03-26", 
#              subject="Spotkanie o godzinie 15:00", 
#              attachments="Załącznik 1, Załącznik 2, Załącznik 3,Załącznik 1, Załącznik 2, Załącznik 3,Załącznik 1, Załącznik 2, Załącznik 3,Załącznik 1, Załącznik 2, Załącznik 3")

# {
#       "name": "export_pdf",
#       "icon": "Qss/icons/icons/font_awesome/regular/file-pdf.png"
# },
# import re
# from pyvis.network import Network
# import networkx as nx
# nx_graph = nx.cycle_graph(10)
# nx_graph.nodes[1]['title'] = 'Number 1'
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10
# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
# nt = Network('500px', '500px')
# # populates the nodes and edges data structures
# nt.from_nx(nx_graph)
# nt.show('nx.html',notebook=False)
    
#multi_part_query(input_string)

# Wyświetlanie wyników
