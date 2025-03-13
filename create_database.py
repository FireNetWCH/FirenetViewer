import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(emails);")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'flag' not in columns:
        cursor.execute("ALTER TABLE emails ADD COLUMN flag INTEGER NOT NULL DEFAULT 0;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT NOT NULL UNIQUE
        );
    ''')

    
    tags = [
        ('Important',),
        ('Work',),
        ('Personal',)
    ]
    cursor.executemany('INSERT OR IGNORE INTO tags (tag_name) VALUES (?);', tags)

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_tags (
            email_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (email_id, tag_id),
            FOREIGN KEY (email_id) REFERENCES emails(id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
        );
    ''')

    
    email_tags = [
        (1, 1),  
        (2, 2),  
        (3, 3)   
    ]
    cursor.executemany('INSERT INTO email_tags (email_id, tag_id) VALUES (?, ?);', email_tags)

    connection.commit()
    print(f"Baza danych '{db_name}' została utworzona i zaktualizowana.")
    connection.close()

if __name__ == "__main__":
    create_database("emails_kukulka.sqlite")
