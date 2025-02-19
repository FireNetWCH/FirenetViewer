import sqlite3

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT NOT NULL UNIQUE
        );
    ''')
    tags = [
        ('Admin',),
        ('Editor',),
        ('Viewer',)
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO tags (tag_name) VALUES (?);
    ''', tags)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            age INTEGER NOT NULL,
            flag INTEGER NOT NULL -- 0 for False, 1 for True
        );
    ''')

    users = [
        ('Alice', 'Smith', '1990-01-15', 34, 1),
        ('Bob', 'Johnson', '1985-07-22', 39, 0),
        ('Charlie', 'Williams', '1992-11-08', 31, 1),
        ('David', 'Brown', '1980-04-25', 44, 0),
        ('John', 'Brown', '1980-04-25', 44, 0),
        ('Tom', 'Born', '1980-04-25', 39, 0),
        ('Luisa', 'Own', '1980-04-25', 44, 0),
        ('Amelia', 'Town', '1980-04-25', 11, 0)
    ]

    cursor.executemany('''
        INSERT INTO users (first_name, second_name, date_of_birth, age, flag)
        VALUES (?, ?, ?, ?, ?);
    ''', users)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_tags (
            user_id INTEGER,
            tag_id INTEGER,
            PRIMARY KEY (user_id, tag_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
        );
    ''')

    user_tags = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 2),
        (8, 3)
    ]

    cursor.executemany('''
        INSERT INTO user_tags (user_id, tag_id) VALUES (?, ?);
    ''', user_tags)

    connection.commit()
    print(f"Database '{db_name}' created and populated with sample data.")
    connection.close()

if __name__ == "__main__":
    create_database("nazwa_bazy.db")
