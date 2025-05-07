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
            print(f"Nie można połączyć z bazą danych SQLite: {db_file}")

    def connect_to_db(self,db_file):
        """Łaczy z wskazaną bazą danych SQLite"""
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
            print(f"Błąd podczas połączenia z bazą danych: {e}")
            return None
    
    def close_connection(self):
        """Zamyka połączenie z bazą danych SQLite"""
        if self.connection:
            self.connection.close()
            logger.info("Zamknięto połączenie z bazą danych SQLite")
        else:
            logger.error("Nie można zamknąć połączenia, ponieważ nie jest otwarte")
            print("Nie można zamknąć połączenia, ponieważ nie jest otwarte") 
    
    def get_all_os_users(self):
        """Pobiera wszystkich użytkowników systemu operacyjnego z bazy danych"""
        try:
            self.cursor.execute("SELECT * FROM os_users")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania użytkowników systemu operacyjnego: {e}")
            print(f"Błąd podczas pobierania użytkowników systemu operacyjnego: {e}")
            return None
    
    def get_software_info(self):
        """Pobiera informacje o oprogramowaniu z bazy danych"""
        try:
            self.cursor.execute("SELECT * FROM system_software_info")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o oprogramowaniu: {e}")
            print(f"Błąd podczas pobierania informacji o oprogramowaniu: {e}")
            return None
        
    def get_device_info(self):
        """Pobiera informacje o urządzeniu z bazy danych"""
        try:
            self.cursor.execute("SELECT * FROM device_info")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o urządzeniu: {e}")
            print(f"Błąd podczas pobierania informacji o urządzeniu: {e}")
            return None
    
    def get_detected_browsers(self):
        """Pobiera wykryte przeglądarki z bazy danych"""

        try:
            self.cursor.execute("SELECT * FROM detected_browsers")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania wykrytych przeglądarek: {e}")
            print(f"Błąd podczas pobierania wykrytych przeglądarek: {e}")
            return None
        
    def get_instaled_software(self):
        """Pobiera zainstalowane oprogramowanie z bazy danych"""
        try:
            self.cursor.execute("SELECT * FROM installed_software")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania zainstalowanego oprogramowania: {e}")
            print(f"Błąd podczas pobierania zainstalowanego oprogramowania: {e}")
            return None
    
    def get_network_config(self):
        """Pobiera konfigurację sieci z bazy danych"""
        try:
            self.cursor.execute("SELECT * FROM network_config")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania konfiguracji sieci: {e}")
            print(f"Błąd podczas pobierania konfiguracji sieci: {e}")
            return None
        
    def get_url_paths_from_browsers(self,browser_name):
        """Pobiera ścieżki id,URL, ścieżke docelową z bazy danych
            Przerobić na łączone pobieranie a nie na pojedyncze przeglądarki
        """
        try:
            self.cursor.execute(f"SELECT id,url, download_path FROM {browser_name}")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania ścieżek URL z przeglądarek: {e}")
            print(f"Błąd podczas pobierania ścieżek URL z przeglądarek: {e}")
            return None

    def get_download_deteils(self,browser_name,id_download):
        """Pobiera szczegóły wybranego rekordu pobierania z bazy danych"""
        try:
            self.cursor.execute(f"SELECT * FROM {browser_name} WHERE id = ?", (id_download,))
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów pobierania: {e}")
            print(f"Błąd podczas pobierania szczegółów pobierania: {e}")
            return None
        
    def get_history_deteils(self,browser_name,id_page):
        """Pobiera szczegóły wybranego rekordu historii przeglądania z bazy danych"""
        try:
            self.cursor.execute(f"""
            SELECT h.id ,h.url, h.title, h.visit_count, h.first_visit_date,h.last_visit_date, d.profile_name FROM {browser_name} 
            as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id
            WHERE h.id = {id_page}""")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów historii: {e}")
            print(f"Błąd podczas pobierania szczegółów historii: {e}")
            return None
        
    def get_all_history(self,browser_name):
        """Pobiera wszystkie rekordy historii przeglądania z bazy danych"""
        try:
            self.cursor.execute(f"""SELECT h.id ,h.url, h.title, h.visit_count, h.first_visit_date,h.last_visit_date, d.profile_name FROM {browser_name} 
                                as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id""")
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania historii: {e}")
            print(f"Błąd podczas pobierania historii: {e}")
            return None

    def get_history_browser_list(self):
        """Pobiera listę przeglądarek, które zawierają historie przeglądania"""
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            table_db_list = self.cursor.fetchall()
            history_tables = []
            for table in table_db_list:
                if table[0].endswith("_history") and not table[0].startswith("usb_"):
                    history_tables.append(table[0])
            return history_tables
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania listy przeglądarek zawierających historie: {e}")
            print(f"Błąd podczas pobierania listy przeglądarek zawierających historie: {e}")
            return None
        
    def get_history_browser_from_all_browser(self,history_browser_list, history_browser_filters,history_browser_marge_filters,LIMIT=100, OFFSET=0):
        """Pobiera historię przeglądania z wszystkich tabel przeglądarek w z listy history_browser_list"""
        full_query = "SELECT h.id ,h.url, h.title, h.visit_count, h.first_visit_date, d.profile_name, full_name,d.name FROM ("
        for index, table in enumerate(history_browser_list):
            full_query += self.generate_part_history_browser_query(table,history_browser_filters)
            is_last = index == len(history_browser_list) - 1
            if is_last:
                # tu dodać filtr na dołączne dane 
                marge_filters = self.generate_part_history_browser_filers_marge_query(history_browser_marge_filters)
                full_query += f""") AS h
                LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                LEFT JOIN os_users AS u ON d.user_id = u.id
                {marge_filters}
                LIMIT {LIMIT} OFFSET {OFFSET}"""
                #np. po ostanim left join dodac u.full_name = "JAN KOWALSKI" itd. 
            else:
                full_query += " UNION ALL "
        print(full_query)
        self.cursor.execute(full_query)
        return self.cursor.fetchall()
    
    def generate_part_history_browser_filers_marge_query(self,history_browser_filters):
        """Generuje część zapytanie do histori przeglądaerek dla połączonych tabel"""
        part_query = ""
        one_filter = True

        if history_browser_filters:
            for key, value in history_browser_filters.items(): 
                if value != "":
                    if one_filter:
                        part_query += f" WHERE {key} LIKE '%{value}%'"
                        one_filter = False
                    else:
                        part_query += f" AND {key} LIKE '%{value}%'"
        else:
            return part_query
        
        return part_query
        

    def generate_part_history_browser_query(self,table_name,history_browser_filters):
        """Generuje część zapytania SQL dla historii przeglądania zawierająca filtry"""
        part_query = f"SELECT * FROM {table_name}"
        one_filter = True
        
        if history_browser_filters:
            for key, value in history_browser_filters.items():
                if key == "visit_count":
                    if value != "0":
                        if one_filter:
                            part_query += f" WHERE {key} > '{value}'"
                            one_filter = False
                        else:
                            part_query += f" AND {key} > '{value}'"
                elif (key == "start_date"):
                    print("start_date")
                    if value != "":
                        if one_filter:
                            part_query += f" WHERE first_visit_date > '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND first_visit_date > '{value}' "
                elif (key == "end_date"):
                    print("end_date")
                    if value != "":
                        if one_filter:
                            part_query += f" WHERE first_visit_date < '{value} "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND first_visit_date < '{value} '"
                else: 
                    if value != "":
                        if one_filter:
                            part_query += f" WHERE {key} LIKE '%{value}%'"
                            one_filter = False
                        else:
                            part_query += f" AND {key} LIKE '%{value}%'"
        else:
            return part_query
        
        return part_query
        