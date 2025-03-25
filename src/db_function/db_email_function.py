import sqlite3
import logging

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

def tag_query_part_generator(active_filters):
        if active_filters['tag'] !="" :
            return f"HAVING t.tag_name in {active_filters['tag']}"
        else:
            return ""
        
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