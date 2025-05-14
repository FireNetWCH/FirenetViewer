import sqlite3
import logging
import pandas as pd
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class database_pc_manager:
    def __init__(self, os_db_file):
        self.connection_os_db = self.connect_to_db(os_db_file)
        self.db_os_name = os_db_file.removesuffix('.db')
    
        if self.connection_os_db:
            self.os_cursor = self.connection_os_db.cursor()
            logger.info(f"Połączono z bazą danych SQLite Os: {os_db_file}")
        else:
            logger.error(f"Nie można połączyć z bazą danych SQLite: {os_db_file}")
            print(f"Nie można połączyć z bazą danych SQLite: {os_db_file}")

        print(self.connection_os_db)

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
        if self.connection_os_db:
            self.connection_os_db.close()
            logger.info("Zamknięto połączenie z bazą danych SQLite")
        else:
            logger.error("Nie można zamknąć połączenia, ponieważ nie jest otwarte")
            print("Nie można zamknąć połączenia, ponieważ nie jest otwarte") 
    
    def get_all_os_users(self):
        """Pobiera wszystkich użytkowników systemu operacyjnego z bazy danych"""
        try:
            self.os_cursor.execute("SELECT * FROM os_users")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania użytkowników systemu operacyjnego: {e}")
            print(f"Błąd podczas pobierania użytkowników systemu operacyjnego: {e}")
            return None
    
    def get_software_info(self):
        """Pobiera informacje o oprogramowaniu z bazy danych"""
        try:
            self.os_cursor.execute("SELECT * FROM system_software_info")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o oprogramowaniu: {e}")
            print(f"Błąd podczas pobierania informacji o oprogramowaniu: {e}")
            return None
        
    def get_device_info(self):
        """Pobiera informacje o urządzeniu z bazy danych"""
        try:
            self.os_cursor.execute("SELECT * FROM device_info")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania informacji o urządzeniu: {e}")
            print(f"Błąd podczas pobierania informacji o urządzeniu: {e}")
            return None
    
    def get_detected_browsers(self):
        """Pobiera wykryte przeglądarki z bazy danych"""

        try:
            self.os_cursor.execute("SELECT * FROM detected_browsers")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania wykrytych przeglądarek: {e}")
            print(f"Błąd podczas pobierania wykrytych przeglądarek: {e}")
            return None
        
    def get_instaled_software(self):
        """Pobiera zainstalowane oprogramowanie z bazy danych"""
        try:
            self.os_cursor.execute("SELECT * FROM installed_software")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania zainstalowanego oprogramowania: {e}")
            print(f"Błąd podczas pobierania zainstalowanego oprogramowania: {e}")
            return None
    
    def get_network_config(self):
        """Pobiera konfigurację sieci z bazy danych"""
        try:
            self.os_cursor.execute("SELECT * FROM network_config")
            rows = self.os_cursor.fetchall()
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
            self.os_cursor.execute(f"SELECT id,url, download_path FROM {browser_name}")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania ścieżek URL z przeglądarek: {e}")
            print(f"Błąd podczas pobierania ścieżek URL z przeglądarek: {e}")
            return None
        
# HISTORY
    def get_history_deteils(self,browser_name,id_page):
        """Pobiera szczegóły wybranego rekordu historii przeglądania z bazy danych"""
        try:
            self.os_cursor.execute(f"""
            SELECT h.id ,h.url, h.title, h.visit_count, h.first_visit_date,h.last_visit_date, d.profile_name FROM {browser_name} 
            as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id
            WHERE h.id = {id_page}""")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów historii: {e}")
            print(f"Błąd podczas pobierania szczegółów historii: {e}")
            return None
        
    def get_all_history(self,browser_name):
        """Pobiera wszystkie rekordy historii przeglądania z bazy danych"""
        try:
            self.os_cursor.execute(f"""SELECT h.id ,h.url, h.title, h.visit_count, h.first_visit_date,h.last_visit_date, d.profile_name FROM {browser_name} 
                                as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id""")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania historii: {e}")
            print(f"Błąd podczas pobierania historii: {e}")
            return None

    def get_browser_table_type_list(self,table_type_name):
        """Pobiera listę przeglądarek, które zawierają historie przeglądania"""
        try:
            self.os_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            table_db_list = self.os_cursor.fetchall()
            history_tables = []
            for table in table_db_list:
                if table[0].endswith(table_type_name) and not table[0].startswith("usb_"):
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
                marge_filters = self.generate_part_history_browser_filers_marge_query(history_browser_marge_filters)
                full_query += f""") AS h
                LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                LEFT JOIN os_users AS u ON d.user_id = u.id
                {marge_filters}
                LIMIT {LIMIT} OFFSET {OFFSET}"""
            else:
                full_query += " UNION ALL "
        rows = self.os_cursor.execute(full_query)
        columns = [desc[0] for desc in self.os_cursor.description]
        return pd.DataFrame(rows, columns=columns)
    def get_sercher_deteils(self,browser_name,id_page):
        """Pobiera szczegóły wybranego rekordu loginów z bazy danych"""
        try:
            self.os_cursor.execute(f"""
            SELECT h.id  , h.url,h.term, h.last_visit_time FROM {browser_name} 
            as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id
            WHERE h.id = {id_page}""")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów zapisanych loginów: {e}")
            print(f"Błąd podczas pobierania szczegółów zapisanych loginów: {e}")
            return None
    
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
        
#DOWNLOAD HISTORY
    def get_download_deteils(self,browser_name,id_download):
        """Pobiera szczegóły wybranego rekordu pobierania z bazy danych"""
        try:
            self.os_cursor.execute(f"SELECT * FROM {browser_name} WHERE id = ?", (id_download,))
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów pobierania: {e}")
            print(f"Błąd podczas pobierania szczegółów pobierania: {e}")
            return None    

    def generate_part_download_history_browser_query(self,table_name,history_download_browser_filters):
        """Generuje część zapytania SQL dla historii pobierania zawierająca filtry"""
        part_query = f"SELECT * FROM {table_name}"
        one_filter = True
        
        if history_download_browser_filters:
            for key, value in history_download_browser_filters.items():
                if key == "file_size":
                    if value != "0":
                        if one_filter:
                            part_query += f" WHERE {key} > '{value}'"
                            one_filter = False
                        else:
                            part_query += f" AND {key} > '{value}'"
                elif (key == "start_time"):
                    if value != "":
                        if one_filter:
                            part_query += f" WHERE start_time > '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND start_time > '{value}' "
                elif (key == "end_time"):
                    if value != "":
                        if one_filter:
                            part_query += f" WHERE start_time < '{value} "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND start_time < '{value} '"
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

    

    def get_download_history_browser_from_all_browser(self,download_history_browser_list, download_history_browser_filters,download_history_browser_marge_filters,LIMIT=100, OFFSET=0):
        full_query = "SELECT h.id , url, download_path ,h.start_time ,d.profile_name, full_name,d.name FROM("
        for index, table in enumerate(download_history_browser_list):
            full_query += self.generate_part_download_history_browser_query(table,download_history_browser_filters)
            is_last = index == len(download_history_browser_list) - 1
            if is_last:
                marge_filters = self.generate_part_history_browser_filers_marge_query(download_history_browser_marge_filters)
                full_query += f""") AS h
                LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                LEFT JOIN os_users AS u ON d.user_id = u.id
                {marge_filters}
                LIMIT {LIMIT} OFFSET {OFFSET}"""
            else:
                full_query += " UNION ALL "
                
        print(full_query)
        self.os_cursor.execute(full_query)
        return self.os_cursor.fetchall()

    def get_download_count_row(self,download_history_browser_list, download_history_browser_filters,download_history_browser_marge_filters,part_generator):
        full_query = "SELECT count() FROM("
        for index, table in enumerate(download_history_browser_list):
            full_query += part_generator(table,download_history_browser_filters)
            is_last = index == len(download_history_browser_list) - 1
            if is_last:
                marge_filters = self.generate_part_history_browser_filers_marge_query(download_history_browser_marge_filters)
                full_query += f""") AS h
                LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                LEFT JOIN os_users AS u ON d.user_id = u.id
                {marge_filters}"""
            else:
                full_query += " UNION ALL "
        print(full_query)
        self.os_cursor.execute(full_query)
        return self.os_cursor.fetchall()
    
### LOGINY 

    def get_all_save_logins(self,browser_list, save_login_filters,download_history_browser_marge_filters,LIMIT=100, OFFSET=0):
        full_query = "SELECT h.id , url ,h.username,h.last_used ,d.profile_name, full_name,d.name FROM("
        print(browser_list)
        for index, table in enumerate(browser_list):
            full_query += self.generate_save_login_part_query(table,save_login_filters)
            is_last = index == len(browser_list) - 1
            if is_last:
                marge_filters = self.generate_part_history_browser_filers_marge_query(download_history_browser_marge_filters)
                full_query += f""") AS h
                LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                LEFT JOIN os_users AS u ON d.user_id = u.id
                {marge_filters}
                LIMIT {LIMIT} OFFSET {OFFSET}"""
            else:
                full_query += " UNION ALL "
        print(full_query)
        self.os_cursor.execute(full_query)
        return self.os_cursor.fetchall()

    def generate_save_login_part_query(self,table_name,save_login_filters):
        """Generuje część zapytania SQL dla historii pobierania zawierająca filtry"""
        part_query = f"SELECT * FROM {table_name}"
        one_filter = True
        
        if save_login_filters:
            for key, value in save_login_filters.items():
                
                if (key == "start_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_used > '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_used > '{value}' "
                elif (key == "end_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_used < '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_used < '{value}'"
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
    

    def get_logins_deteils(self,browser_name,id_page):
        """Pobiera szczegóły wybranego rekordu loginów z bazy danych"""
        try:
            self.os_cursor.execute(f"""
            SELECT h.id ,h.url, h.last_used, d.profile_name FROM {browser_name} 
            as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id
            WHERE h.id = {id_page}""")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania szczegółów zapisanych loginów: {e}")
            print(f"Błąd podczas pobierania szczegółów zapisanych loginów: {e}")
            return None
        
    # SEARCH HISTORY
            
    def get_all_seracher(self,browser_list, save_login_filters,download_history_browser_marge_filters,LIMIT=100, OFFSET=0):
            full_query = "SELECT h.id  ,h.term, url,h.last_visit_time ,d.profile_name, full_name,d.name FROM("
            print(browser_list)
            for index, table in enumerate(browser_list):
                full_query += self.generate_sarcher_part_query(table,save_login_filters)
                is_last = index == len(browser_list) - 1
                if is_last:
                    marge_filters = self.generate_part_history_browser_filers_marge_query(download_history_browser_marge_filters)
                    full_query += f""") AS h
                    LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                    LEFT JOIN os_users AS u ON d.user_id = u.id
                    {marge_filters}
                    LIMIT {LIMIT} OFFSET {OFFSET}"""
                else:
                    full_query += " UNION ALL "
            print(full_query)
            self.os_cursor.execute(full_query)
            return self.os_cursor.fetchall()
    
    def generate_sarcher_part_query(self,table_name,sercher_filters):
        """Generuje część zapytania SQL dla historii pobierania zawierająca filtry"""
        part_query = f"SELECT * FROM {table_name}"
        one_filter = True
        
        if sercher_filters:
            for key, value in sercher_filters.items():
                
                if (key == "start_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_visit_time > '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_visit_time > '{value}' "
                elif (key == "end_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_visit_time < '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_visit_time < '{value}'"
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
    
    #AUTOFILL

    def get_all_autofill(self,browser_list, autofill_filters,download_history_browser_marge_filters,LIMIT=100, OFFSET=0):
            full_query = "SELECT h.id  ,h.fieldname, h.value, h.last_used ,d.profile_name, full_name,d.name FROM("
            print(browser_list)
            for index, table in enumerate(browser_list):
                full_query += self.generate_autofill_part_query(table,autofill_filters)
                is_last = index == len(browser_list) - 1
                if is_last:
                    marge_filters = self.generate_part_history_browser_filers_marge_query(download_history_browser_marge_filters)
                    full_query += f""") AS h
                    LEFT JOIN detected_browsers AS d ON h.browser_id = d.id
                    LEFT JOIN os_users AS u ON d.user_id = u.id
                    {marge_filters}
                    LIMIT {LIMIT} OFFSET {OFFSET}"""
                else:
                    full_query += " UNION ALL "
            print(full_query)
            self.os_cursor.execute(full_query)
            return self.os_cursor.fetchall()
    

    def generate_autofill_part_query(self,table_name,sercher_filters):
        """Generuje część zapytania SQL dla historii pobierania zawierająca filtry"""
        part_query = f"SELECT * FROM {table_name}"
        one_filter = True
        
        if sercher_filters:
            for key, value in sercher_filters.items():
                
                if (key == "start_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_used > '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_used > '{value}' "
                elif (key == "end_date"):
                    if value != "":
                        print(key)
                        if one_filter:
                            part_query += f" WHERE last_used < '{value}' "
                            one_filter = False
                        else:
                            part_query = part_query +f" AND last_used < '{value}'"
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
    
    def get_autofill_deteils(self,browser_name,id_row):
        """Pobiera szczegóły wybranego rekordu autouzupelniania z bazy danych"""
        try:
            self.os_cursor.execute(f"""
            SELECT h.id , fieldname, h.value,h.times_used, h.creation_date, h.last_used, d.profile_name FROM {browser_name} 
            as h LEFT JOIN detected_browsers as d ON h.browser_id = d.id
            WHERE h.id = {id_row}""")
            rows = self.os_cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobiera szczegóły wybranego rekordu autouzupelniania z bazy danych: {e}")
            print(f"Błąd podczas pobiera szczegóły wybranego rekordu autouzupelniania z bazy danych: {e}")
            return None

   
    
                                
