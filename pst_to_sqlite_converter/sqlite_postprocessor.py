import sqlite3, os

def get_available_folder_name(parent_dir, base_name):
    candidate = base_name
    counter = 2
    while os.path.exists(os.path.join(parent_dir, candidate)):
        candidate = f"{base_name}_{counter}"
        counter += 1
    return candidate

def rename_db_and_directory(old_path, new_folder_name, new_db_name):
    old_dir = os.path.dirname(old_path)
    old_db_name = os.path.basename(old_path)

    parent_dir = os.path.dirname(old_dir)

    final_folder_name = get_available_folder_name(parent_dir, new_folder_name)
    new_dir = os.path.join(parent_dir, final_folder_name)

    os.rename(old_dir, new_dir)

    base_db_name, ext = os.path.splitext(new_db_name)
    if final_folder_name != new_folder_name:
        base_db_name = final_folder_name
    final_db_name = base_db_name + ext

    old_db_path = os.path.join(new_dir, old_db_name)
    new_db_path = os.path.join(new_dir, final_db_name)
    os.rename(old_db_path, new_db_path)

    print(f"Database renamed to: {new_db_path}")
    return new_db_path

def postprocess_sqlite(db_name):
    new_name_bool = False
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    cursor.execute('''ALTER TABLE folders ADD COLUMN item_count INTEGER;''')
    cursor.execute('''UPDATE folders SET item_count = (SELECT COUNT(*) FROM emails WHERE emails.folder_id = folders.id);''')
    cursor.execute('''
    UPDATE folders
        SET item_count = (
            SELECT SUM(item_count)
            FROM folders
            WHERE id >= 2
        )
        WHERE id = 1;
        ''')
    cursor.execute('''
    UPDATE folders
        SET item_count = (
            SELECT SUM(item_count)
            FROM folders
            WHERE id = 1
        )
        where path like "%Najwyższy poziom pliku danych programu Outlook";''')
    
    connection.commit()

    cursor.execute("""
    SELECT id FROM folders
    WHERE LOWER(path) LIKE '%sent'
    ORDER BY id ASC
    LIMIT 1
    """)
    id_result = cursor.fetchone()
    if id_result:
        folder_id = id_result[0]
        cursor.execute("""
        SELECT sender_email FROM emails
        WHERE folder_id = ?
        ORDER BY id ASC
        LIMIT 1
        """, (folder_id,))
        mail_result = cursor.fetchone()
        if mail_result:
            new_name_bool = True
            email = mail_result[0]
    cursor.close()
    connection.close()

    if new_name_bool:
        rename_db_and_directory(db_name, email,email)

if __name__=="__main__":
    sqlite_root = "E:\\sqlite_with_headers 3.0"
    counter = 0

    for root,dirs,files in os.walk(sqlite_root):
        for file in files:
            if file.endswith("sqlite"):
                postprocess_sqlite(os.path.join(root,file))
                print(f"Zaktualizowano bazę {file}.")
                counter += 1

    print(f"Przetworzono {counter} baz sqlite.")