import sqlite3
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class database_file_export_menager:
    def __init__(self, os_db_file):
        self.connection_file_export_db = self.connect_to_db(os_db_file)
        self.db_file_export_name = os_db_file.removesuffix('.db')
        if self.connection_file_export_db:
            self.cursor = self.connection_file_export_db.cursor()
            logger.info(f"Połączono z bazą danych SQLite file_export: {os_db_file}")
        else:
            logger.error(f"Nie można połączyć z bazą danych SQLite : {os_db_file}")
            print(f"Nie można połączyć z bazą danych SQLite: {os_db_file}")

    def connect_to_db(self,db_file):
        """Łaczy z wskazaną bazą danych SQLite"""
        try:
            connection = sqlite3.connect(db_file)
            print("Połączono z bazą danych SQLite")
            cursor = connection.cursor()
            cursor.execute("SELECT sqlite_version();")
            sqlite_version = cursor.fetchone()
            print(f"Wersja SQLite: {sqlite_version[0]}")
            #self.connection_os_db = connection
            return connection
        except sqlite3.Error as e:
            print(f"Błąd podczas połączenia z bazą danych: {e}")
            logger.error(f"Błąd podczas połączenia z bazą danych: {e}")
            print(f"Błąd podczas połączenia z bazą danych: {e}")
            return None
    
    def close_connection(self):
        """Zamyka połączenie z bazą danych SQLite"""
        if self.connection_file_export_db:
            self.connection_file_export_db.close()
            logger.info("Zamknięto połączenie z bazą danych SQLite")
        else:
            logger.error("Nie można zamknąć połączenia, ponieważ nie jest otwarte")
            print("Nie można zamknąć połączenia, ponieważ nie jest otwarte") 

    def get_all_table_list(self):
        """Pobiera liste wszystkich tabel z file_export_by_typy"""
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            table_db_list = self.cursor.fetchall()
            return table_db_list
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania listy przeglądarek zawierających historie: {e}")
            print(f"Błąd podczas pobierania listy przeglądarek zawierających historie: {e}")
            return None
        
    def get_contents_from_table(self,table_name):
        """Pobiera zawartość ze wskazanej tabeli wyeksportowanych plików"""
        try:
            self.cursor.execute(f"SELECT id, file_name,file_size, date_created FROM {table_name} ORDER BY date_created LIMIT 100")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania zawartości tabeli {table_name}: {e}")
            print(f"Błąd podczas pobierania zawartości tabeli {table_name}: {e}")
            return None