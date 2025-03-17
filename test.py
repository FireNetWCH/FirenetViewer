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