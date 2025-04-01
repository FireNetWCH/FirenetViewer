import sqlite3
import logging
import re
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def connect_to_database(self, db_name: str) -> None:
        """Nawiązuje połączenie z bazą danych SQLite."""
        try:
           
            self.db_connection = sqlite3.connect(db_name)
            logger.info(f"Połączono z bazą danych {db_name}")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas łączenia z bazą danych:{db_name} {e}")
            print(f"Błąd podczas łączenia z bazą danych:{db_name} {e}")
            self.db_connection = None
        
def apply_filters(active_filters) -> None:
        """
        Zwraca fragmęt zapytania SQL zawierający filtry 
        """
        query_part = ""
        firtFiltr = True
        #print(self.active_filters)
        for key, value in active_filters.items():
            if key == "folder_id" and str(value) == "1":
                print(f"{key} +{value}")
            elif(key == "tag"):
                pass
            
            elif (key == "date_fr"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE date > '{value}'"
                        firtFiltr = False
                    else:
                        query_part = query_part +f"AND date > '{value}'"
            elif (key == "date_to"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE date < '{value}'"
                        firtFiltr = False
                    else:
                        query_part = query_part +f"AND date < '{value}'"

            elif(key == "body"):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE REPLACE(body, X'200C', '') LIKE '%{value}%' COLLATE NOCASE"
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND REPLACE(body, X'200C', '') LIKE '%{value}%' COLLATE NOCASE"
            elif(key == "folder_id"):
                if value != "" :
                    if firtFiltr:
                        query_part = f"WHERE {key} LIKE '{value}' COLLATE NOCASE "
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND {key} LIKE '{value}' COLLATE NOCASE "
            elif(key == "flag"):
                if value == "True":
                    if firtFiltr:
                        query_part = f"WHERE {key} LIKE {value}"
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND {key} LIKE {value}"
            else:
                if value != "" :
                    if firtFiltr:
                        query_part = f"WHERE {key} LIKE '%{value}%' COLLATE NOCASE "
                        firtFiltr = False
                    else:
                        query_part = query_part + f"AND {key} LIKE '%{value}%' COLLATE NOCASE "

        return query_part

def tag_query(filters):
    """Generuje zapytanie umorzliwające selekcje po wybranych tagach"""
    query=  f'''WITH filtered_tags AS (
    SELECT et.email_id, t.tag_name
    FROM email_tags et
    JOIN tags t ON et.tag_id = t.id
    WHERE t.tag_name IN {filters['tag']}
    )
    SELECT e.id, e.sender_name, e.cc, e.subject, e.date, e.flag,
        GROUP_CONCAT(ft.tag_name) AS tags
    FROM emails e
    JOIN filtered_tags ft ON e.id = ft.email_id
    {apply_filters(filters)}
    GROUP BY e.id
    LIMIT 500 OFFSET 0;'''

    return query

def update_multi_flags(db_connection,id_list,state):
    """Ustawia wybrany stan flagi na liście emaili"""
    cursor = db_connection.cursor()
    placeholders = ", ".join(["?"] * len(id_list))
    print(placeholders)
    query = f"UPDATE emails SET flag = ? WHERE id IN ({placeholders})"
    cursor.execute(query, (state, *id_list))
    db_connection.commit()

    
def update_flag(db_connection, email_id: int, state: int) -> None:
        """Aktualizuje flagę użytkownika w bazie danych."""
        flag_value = 1 if state else 0
        try:
            cursor = db_connection.cursor()
            cursor.execute("UPDATE emails SET flag = ? WHERE id = ?", (flag_value, email_id))
            db_connection.commit()
            logger.info(f"Updated flag for emails ID {email_id} to {flag_value}.")
        except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizacji flagi: {e}")
            print(f"Błąd podczas aktualizacji flagi: {e}")

def emails_to_export(db_connection,filters = None,list = None):
    """Zwraca id,date,sender_name,recipients, subject, body wraz z listą załączników wiadomości o flagowanych"""
    try:
        print(list)
        cursor = db_connection.cursor()
        if (filters is None) and (list is None):
            query="""
            SELECT e.id,e.date, e.sender_name, e.recipients, e.subject , e.body,
            GROUP_CONCAT(a.attachment_filename) AS atach
            FROM emails e
            LEFT JOIN attachments a ON e.id = a.email_id
            WHERE flag = '1'
            GROUP BY e.id
            """
            cursor.execute(query)
        elif filters is not None:
            query=f"""
            SELECT e.id,e.date, e.sender_name, e.recipients, e.subject , e.body,
            GROUP_CONCAT(a.attachment_filename) AS atach
            FROM emails e
            LEFT JOIN attachments a ON e.id = a.email_id
            {apply_filters(filters)}
            GROUP BY e.id
            """
            cursor.execute(query)
        elif list is not None:
            placeholders = ", ".join(["?"] * len(list))
            query=f"""
            SELECT e.id,e.date, e.sender_name, e.recipients, e.subject , e.body,
            GROUP_CONCAT(a.attachment_filename) AS atach
            FROM emails e
            LEFT JOIN attachments a ON e.id = a.email_id
            WHERE e.id in ({placeholders})
            GROUP BY e.id
            """
            cursor.execute(query,list)
        
        
        results = cursor.fetchall()
        print(results)
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania wiadomości z flagami: {e}")
        print(f"Błąd podczas pobierania wiadomości z flagami: {e}")
    return results

def get_all_labels_name(db_connection):
    """Zwraca wszystki wartości z tabeli labels_name"""
    try:
        query="""
        SELECT * from labels_name
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania z tabeli labels_name: {e}")
        print(f"Błąd podczas pobierania z tabeli labels_name: {e}")

def add_label(db_connection,id_label_name,id_email,label_text):
    """Dodaje rekord do bazy danych labels"""
    try:
        query=f"""
        INSERT INTO email_labels ("label", "id_labels_name", "id_email") VALUES ('{label_text}', {id_label_name}, {id_email});
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas dodawania do tabeli email_labels: {e}")
        print(f"Błąd podczas dodawania do tabeli email_labels: {e}")

def delate_tag(db_connection,id_tag):
    """Usuwa tag o wskazanym id"""
    try:
        query = f""" 
        DELETE FROM tags where id = {id_tag} 
        """
        print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        print("")
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas usuwania taga z tabeli tags: {e}")
            print(f"Błąd podczas usuwania taga z tabeli tags: {e}")

def updata_tag(db_connection,id_tag,new_tag_name):
    """Uaktualnia nazwę wskazanego tagu"""
    try:
        query = f"""
        UPDATE tags set tag_name = '{new_tag_name}' WHERE ID = {id_tag}
        """
        print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizowania tagów: {e}")
            print(f"Błąd podczas aktualizowania tagów: {e}")

