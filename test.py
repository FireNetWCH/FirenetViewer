# import sqlite3


# conn = sqlite3.connect("D:\\SQL\\spiatek\\spiatek.sqlite")
# cursor = conn.cursor()
# cursor.execute('SELECT sqlite_version();')
# version = cursor.fetchone()
# print(f"SQLite Version: {version[0]}")
# # conn.text_factory = str
# cursor = conn.cursor()

# query = '''
#     SELECT e.id, e.sender_name, e.cc, e.subject, e.date, e.flag,
#            GROUP_CONCAT(t.tag_name) AS tags
#     FROM emails e
#     LEFT JOIN email_tags et ON e.id = et.email_id
#     LEFT JOIN tags t ON et.tag_id = t.id
#     WHERE REPLACE(body, X'200C', '') LIKE '%piwo%' COLLATE NOCASE
#     GROUP BY e.id
#     LIMIT 500 OFFSET 0
# '''
# # cursor.execute("SELECT body FROM emails LIMIT 5")
# cursor.execute(query,)
# data = cursor.fetchall()

# print(f"Liczba wierszy: {len(data)}")  
# print(data[:5])  

# conn.close()

from PyInstaller.utils.hooks import collect_submodules
collect_submodules('lxml')

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
super().__init__(parent)
        self.file_name = filename
        self.file_path = file_path
        layout = QHBoxLayout(self)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setContentsMargins(1, 1, 1, 1)
        frame_layout = QHBoxLayout(self.frame)
        frame_layout.setContentsMargins(1, 1, 1, 1)
        frame_layout.setSpacing(1)
        self.label = QLabel(filename)
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.preview_button = QPushButton(QIcon("./Qss/icons/black/feather/link.png"), "")
        self.preview_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.preview_button.clicked.connect(self.preview_file)
        frame_layout.addWidget(self.label)
        frame_layout.addWidget(self.preview_button)
        frame_layout.addStretch()
        layout.addWidget(self.frame)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setContentsMargins(1, 5, 1, 5)



	"QPushButton": [
		{
		"name": "show_flags_btn",

      "fallBackStyle": [
        "background-color: #ff0000;"
      ],
      "defaultStyle": [
        "background-color: #ff0000;",
		"hover::{background-color: #0000ff;}"
      ]
		}
	  ]
QCSS
QMainWindow #tableWidget{
    background-color: #ff0000;
    background:#ff0000;
    color: #00ff00;
    ::item{
        background-color: #ff0000
    }
}

#serchEmailFrame{
            background-color: $COLOR_ACCENT_3;
        }