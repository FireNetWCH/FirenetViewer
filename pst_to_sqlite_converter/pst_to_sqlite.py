import pypff
import sqlite3
import re
import os

def migrate_pst(PST_FILE,ATTACHMENTS_DIR,DB_FILE):
    
    def setup_database():
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS folders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emails (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                sender_name TEXT,
                sender_email TEXT,
                recipients TEXT,
                cc TEXT,
                bcc TEXT,
                subject TEXT,
                body TEXT,
                folder_id INTEGER,
                flag INTEGER NOT NULL DEFAULT 0,
                transport_header TEXT,
                FOREIGN KEY (folder_id) REFERENCES folders (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attachments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                attachment_filename TEXT,
                email_id INTEGER,
                FOREIGN KEY (email_id) REFERENCES emails (id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag_name TEXT NOT NULL UNIQUE
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS email_tags (
                email_id INTEGER,
                tag_id INTEGER,
                PRIMARY KEY (email_id, tag_id),
                FOREIGN KEY (email_id) REFERENCES emails(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS email_labels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                label TEXT, 
                id_labels_name INTEGER,
                id_email INTEGER,
                FOREIGN KEY (id_labels_name) REFERENCES labels_name(id) ON DELETE CASCADE,
                FOREIGN KEY (id_email) REFERENCES emails(id) ON DELETE CASCADE
            );
        ''')

        cursor.execute('''
            CREATE TABLE labels_name (
                    id INTEGER NOT NULL UNIQUE,
                    label_name TEXT NOT NULL UNIQUE,
                    PRIMARY KEY(id AUTOINCREMENT)
            );
        ''')

        conn.commit()
        conn.close()

    # Funkcja unifikująca body do typu str, oraz zmieniająca znaki nowej linii na tag <br>
    def convert_body_for_frontend(text):
        if text:
            if isinstance(text, str):
                result_text = text
            else:
                try:
                    result_text = text.decode("utf-8")
                except:
                    result_text = text.decode("ISO-8859-1")
            return result_text.replace('\n', '<br>')
        return text

    # Funkcja czyszcząca listę adresów e-mail (usuwa duplikaty i zbędne znaki)
    def clean_email_list(email_str):
        if not email_str:
            return None
        # Wyszukuje adresy e-mail
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', email_str)
        unique_emails = sorted(set(emails))
        return ", ".join(unique_emails) if unique_emails else None

    # Pobieranie adresu e-mail nadawcy z nagłówków
    def extract_sender_email(transport_headers):
        if transport_headers:
            match = re.search(r"From: .*?<(.*?)>", transport_headers, re.IGNORECASE)
            if match:
                return match.group(1)
            else:
                match = re.search(r"From: (.*)", transport_headers, re.IGNORECASE)
                if match:
                    return match.group(1)
        return None

    # Pobieranie odbiorców (TO, CC, BCC) z nagłówków
    def extract_recipients(transport_headers):
        to_recipients, cc_recipients, bcc_recipients = None, None, None
        if transport_headers:
            to_match = re.search(r"To: (.*)", transport_headers, re.IGNORECASE)
            cc_match = re.search(r"Cc: (.*)", transport_headers, re.IGNORECASE)
            bcc_match = re.search(r"Bcc: (.*)", transport_headers, re.IGNORECASE)

            to_recipients = clean_email_list(to_match.group(1)) if to_match else None
            cc_recipients = clean_email_list(cc_match.group(1)) if cc_match else None
            bcc_recipients = clean_email_list(bcc_match.group(1)) if bcc_match else None

        return to_recipients, cc_recipients, bcc_recipients

    # Pobieranie/utworzenie folderu w bazie; zwraca jego id
    def get_or_create_folder_id(cursor, folder_path):
        folder_path = folder_path.replace("/None",'')
        cursor.execute("SELECT id FROM folders WHERE path = ?", (folder_path,))
        result = cursor.fetchone()
        if result:
            return result[0]
        cursor.execute("INSERT INTO folders (path) VALUES (?)", (folder_path,))
        return cursor.lastrowid

    def shorten_filename(filename, max_length=128):
        if len(filename) <= max_length:
            return filename
        name, ext = os.path.splitext(filename)
        name = name[:max_length - len(ext)]
        return name + ext

    def fix_bad_chars_in_filename(filename):
        forbidden_characters = r'[\\/:*?"<>|]'
        filename = re.sub(forbidden_characters, '_', filename)
        return filename

    def repair_filename(filename):
        ext_dict = {"pdf":"pdf",}
        binary_filename = filename.encode('utf-16')
        
        matches = re.findall(rb'[ -~]+', binary_filename)
        chars = []
        for match in matches:
            if match != None:
                chars.append(match.decode('utf-8'))
        if chars:
            strs_from_binary_filename = "".join(chars)
        
            title_match = re.search(r"Title\((.*?)\)", strs_from_binary_filename)
            if title_match:
                repaired_filename = fix_bad_chars_in_filename(title_match.group(1))
                ext = next((ext_dict.get(k,None) for k in ext_dict.keys() if k in strs_from_binary_filename.lower()), '')
                if ext:
                    repaired_filename = f"{repaired_filename}.{ext}"
                return repaired_filename
        return None
    
    def process_entries(record_set, id):
        entry = record_set.get_entry(id)
        if hasattr(entry, 'get_data'):
            entry_data = entry.get_data()  # Może to zwrócić dane w postaci binarnej
            filename = entry_data.decode('utf-16', errors='replace')
            return filename
        return None
    
    def process_message(message, folder_id, cursor):
        transport_headers = message.transport_headers
        email_date = message.delivery_time.strftime("%Y-%m-%d %H:%M:%S") if message.delivery_time else None
        sender_name = message.sender_name
        sender_email = extract_sender_email(transport_headers)
        to_recipients, cc_recipients, bcc_recipients = extract_recipients(transport_headers)
        subject = message.subject
        body = message.plain_text_body if message.plain_text_body else message.html_body
        body = convert_body_for_frontend(body)

        # Wstawienie rekordu e-mail do bazy
        cursor.execute('''
            INSERT INTO emails (date, sender_name, sender_email, recipients, cc, bcc, subject, body, folder_id, flag, transport_header)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (email_date, sender_name, sender_email, to_recipients, cc_recipients, bcc_recipients, subject, body, folder_id, 0, transport_headers))
        email_id = cursor.lastrowid

        # Próba przetworzenia załączników
        num_attachments = 0
        try:
            num_attachments = message.number_of_attachments
        except:
            num_attachments = 0

        if num_attachments > 0:
            email_attach_dir = os.path.join(ATTACHMENTS_DIR, str(email_id))
            os.makedirs(email_attach_dir, exist_ok=True)
            for i in range(num_attachments):
                try:
                    attachment = message.get_attachment(i)
                except Exception as e:
                    print(f"❌ Błąd pobierania załącznika numer {i} w e-mailu {email_id}: {e}")
                    continue

                # Próba uzyskania oryginalnej nazwy załącznika
                filename = None
                try:
                    if hasattr(attachment, 'record_sets'):
                        for i in range(attachment.get_number_of_record_sets()):
                            record_set = attachment.get_record_set(i)
                            filename = process_entries(record_set, 4)
                            if filename:
                                if filename.startswith("."):
                                    filename = process_entries(record_set, 5)
                            filename = shorten_filename(filename)

                    if filename == "multipart/signed":
                        continue                                
                    
                except Exception as e:
                    print(f"❌ Błąd przy pobierania nazwy dla załącznika {i} w e-mailu {email_id}: {e}")

                if filename:
                    filename = filename.strip()
                    if not filename:
                        filename = None

                # Jeśli nazwa nadal nie została uzyskana, ustaw domyślną
                if not filename:
                    filename = f"attachment_{i}"

                # Odczyt danych załącznika
                try:
                    data = attachment.read_buffer(attachment.size)
                except Exception as e:
                    print(f"❌ Błąd odczytu załącznika w e-mailu {email_id}: {e}") # '{shorten_filename(filename, 30)}'
                    continue

                # Zapis pliku do dedykowanego katalogu
                try:
                    file_path = os.path.join(email_attach_dir, filename)
                    if not os.path.isfile(file_path):
                        with open(file_path, "wb") as f:
                            f.write(data)
                except:
                    try:
                        repaired_filename = repair_filename(filename)
                        if repaired_filename:
                            file_path = os.path.join(email_attach_dir, repaired_filename)
                            if not os.path.isfile(file_path):
                                with open(file_path, "wb") as f:
                                    f.write(data)
                            filename = repaired_filename
                        else:
                            continue
                    except Exception as e:
                        print(f"Błąd zapisu załącznika w e-mailu {email_id}: {e}")
                        continue

                # Wstawienie rekordu załącznika do bazy
                try:
                    cursor.execute('''
                        INSERT INTO attachments (attachment_filename, email_id)
                        VALUES (?, ?)
                    ''', (filename, email_id))
                except Exception as e:
                    print(f"Błąd zapisu rekordu załącznika w bazie dla e-maila {email_id}: {e}")
        return email_id

    # Rekurencyjne przeszukiwanie folderów PST.
    def extract_emails_from_folder(folder, folder_path, cursor):
        folder_id = get_or_create_folder_id(cursor, folder_path)
        
        # Przetwarzanie wiadomości w bieżącym folderze
        for message in folder.sub_messages:
            process_message(message, folder_id, cursor)
        
        # Rekurencyjne przetwarzanie podfolderów
        for subfolder in folder.sub_folders:
            subfolder_path = os.path.join(folder_path, subfolder.name)
            extract_emails_from_folder(subfolder, subfolder_path, cursor)

    # Główna funkcja przetwarzania PST
    def process_pst(pst_file):
        pst = pypff.file()
        pst.open(pst_file)
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        root_folder = pst.get_root_folder()
        root_folder_path = f"/{root_folder.name}"
        extract_emails_from_folder(root_folder, root_folder_path, cursor)
        
        conn.commit()
        conn.close()
        pst.close()

    setup_database()
    process_pst(PST_FILE)
    print(f"Migracja PST zakończona. Dane zapisane w {DB_FILE} oraz załączniki w katalogu {ATTACHMENTS_DIR}")

def main():
    PST_ROOT = "D:\\BERT\\Poczta - dysk H\\Oryginalny format"
    PST_LIST = [
        "xxx.pst",
        "yyy.pst",
    ]
    
    for pst in PST_LIST:
        PST_FILE = os.path.join(PST_ROOT, pst)  # Podaj ścieżkę do pliku PST
        PST_NAME = os.path.basename(PST_FILE)[:-4]
        OUTPUT_DIR = os.path.join("E:\\sqlite_with_headers 3.0",PST_NAME)
        DB_FILE = os.path.join(OUTPUT_DIR, f"{PST_NAME}.sqlite")       
        ATTACHMENTS_DIR = os.path.join(os.path.dirname(DB_FILE), "Attachments")
        os.makedirs(ATTACHMENTS_DIR, exist_ok=True)
        migrate_pst(PST_FILE,ATTACHMENTS_DIR,DB_FILE)

if __name__ == "__main__":
    main()