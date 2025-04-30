import sqlite3
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class database_pc_manager:
    def __init__(self, db_file):
        self.connection = self.connect_to_db(db_file)
        self.db_name = db_file.removesuffix('.db')

        if self.connection:
            self.cursor = self.connection.cursor()
            logger.info(f"Połączono z bazą danych SQLite: {db_file}")
        else:
            logger.error(f"Nie można połączyć z bazą danych SQLite: {db_file}")

    def connect_to_db(self,db_file):
        try:
            connection = sqlite3.connect(db_file)
            print("Połączono z bazą danych SQLite")
            cursor = connection.cursor()
            cursor.execute("SELECT sqlite_version();")
            sqlite_version = cursor.fetchone()
            print(f"Wersja SQLite: {sqlite_version[0]}")
            self.connection = connection
            return connection
        except sqlite3.Error as e:
            print(f"Błąd podczas połączenia z bazą danych: {e}")
            logger.error(f"Błąd podczas połączenia z bazą danych: {e}")
            return None
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            logger.info("Zamknięto połączenie z bazą danych SQLite")
        else:
            logger.error("Nie można zamknąć połączenia, ponieważ nie jest otwarte") 
    
    def get_all_os_users(self):
        try:
            self.cursor.execute("SELECT * FROM os_users")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania użytkowników systemu operacyjnego: {e}")
            return None
    
    def get_software_info(self):
        try:
            self.cursor.execute("SELECT * FROM system_software_info")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o oprogramowaniu: {e}")
            return None
        
    def get_device_info(self):
        try:
            self.cursor.execute("SELECT * FROM device_info")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o urządzeniu: {e}")
            return None
    
    def get_detected_browsers(self):
        try:
            self.cursor.execute("SELECT * FROM detected_browsers")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania wykrytych przeglądarek: {e}")
            return None
        
    def get_instaled_software(self):
        try:
            self.cursor.execute("SELECT * FROM installed_software")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania zainstalowanego oprogramowania: {e}")
            return None
    
    def get_network_config(self):
        try:
            self.cursor.execute("SELECT * FROM network_config")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania konfiguracji sieci: {e}")
            return None

