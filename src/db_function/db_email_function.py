import sqlite3
import logging
import re
import itertools
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



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
                print(f"")
            elif(key == "tag"):
                pass
            
            elif (key == "date_fr"):
                if value != "":
                    if firtFiltr:
                        query_part = f" WHERE date > '{value}' "
                        firtFiltr = False
                    else:
                        query_part = query_part +f" AND date > '{value}' "
            elif (key == "date_to"):
                if value != "":
                    if firtFiltr:
                        query_part = f" WHERE date < '{value} "
                        firtFiltr = False
                    else:
                        query_part = query_part +f" AND date < '{value} '"
        #WHERE REPLACE(body, X'200C', '' )
            elif(key == "body")| (key == 'subject'):
                if value != "":
                    if firtFiltr:
                        query_part = f"WHERE {multi_part_query(key,value)} "
                        firtFiltr = False
                    else:
                        query_part = query_part + f" AND {multi_part_query(key,value)} COLLATE NOCASE "
            elif(key == "folder_id"):
                if value != "" :
                    if firtFiltr:
                        query_part = f" WHERE {key} LIKE '{value}' COLLATE NOCASE "
                        firtFiltr = False
                    else:
                        query_part = query_part + f" AND {key} LIKE '{value}' COLLATE NOCASE "
            elif(key == "flag"):
                if value == "True":
                    if firtFiltr:
                        query_part = f" WHERE {key} LIKE {value} "
                        firtFiltr = False
                    else:
                        query_part = query_part + f" AND {key} LIKE {value}"
            
            else:
                if value != "" :
                    if firtFiltr:
                        query_part = f" WHERE {key} LIKE '%{value}%' COLLATE NOCASE "
                        firtFiltr = False
                    else:
                        query_part = query_part + f" AND {key} LIKE '%{value}%' COLLATE NOCASE "

        return query_part

def tag_query(filters):
    """Generuje zapytanie umorzliwające selekcje po wybranych tagach"""
    print(filters['tag'])
    if '#_empty_#'not in filters['tag']:
        query=  f'''WITH filtered_tags AS (
        SELECT et.email_id, t.tag_name
        FROM email_tags et
        JOIN tags t ON et.tag_id = t.id
        WHERE t.tag_name IN {filters['tag']}
        )
        SELECT e.id, e.sender_email, e.recipients, e.subject, e.date, e.flag, e.cc, e.bcc,
            GROUP_CONCAT(ft.tag_name) AS tags
        FROM emails e
        JOIN filtered_tags ft ON e.id = ft.email_id
        {apply_filters(filters)}
        GROUP BY e.id
        '''
    else :
        _and = ""
        for key, value in filters.items():
            if key == "folder_id":
                if str(value) != "1":
                    _and = 'AND'      
            elif key == "flag":
                if value != "False":
                    _and = 'AND'
            elif key == "tag":
                pass        
            elif value != "":
                _and = 'AND'
            

        query=  f'''SELECT e.id, e.sender_email, e.recipients, e.subject, e.date, e.flag, e.cc,e.bcc,
                    GROUP_CONCAT(t.tag_name) AS tags 
                FROM emails e
                LEFT JOIN email_tags et ON e.id = et.email_id
                LEFT JOIN tags t ON et.tag_id = t.id
                WHERE e.id NOT IN (SELECT DISTINCT email_id FROM email_tags)
                {_and} {apply_filters(filters).replace('WHERE',"")}
                GROUP BY e.id
        '''
        # query = f'''SELECT id, sender_email, recipients, subject, date, flag, cc, bcc FROM emails 
        # WHERE id NOT IN (SELECT DISTINCT email_id FROM email_tags)
        # {apply_filters(filters)}
        # '''
    return query

def update_multi_flags(db_connection,id_list,state):
    """Ustawia wybrany stan flagi na liście emaili"""
    cursor = db_connection.cursor()
    placeholders = ", ".join(["?"] * len(id_list))
    #print(placeholders)
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
    """Zwraca id,date,sender_email,recipients, subject, body wraz z listą załączników wiadomości o flagowanych"""
    try:
        #print(list)
        cursor = db_connection.cursor()
        if (filters is None) and (list is None):
            query="""
            SELECT e.id,e.date, e.sender_email, e.recipients, e.subject , e.body,
            GROUP_CONCAT(a.attachment_filename) AS atach
            FROM emails e
            LEFT JOIN attachments a ON e.id = a.email_id
            WHERE flag = '1'
            GROUP BY e.id
            """
            cursor.execute(query)
        elif filters is not None:
            if filters['tag'] == "" :
                query=f"""
                SELECT e.id,e.date, e.sender_email, e.recipients, e.subject , e.body,
                GROUP_CONCAT(a.attachment_filename) AS atach
                FROM emails e
                LEFT JOIN attachments a ON e.id = a.email_id
                {apply_filters(filters)}
                GROUP BY e.id
                """
            else: 
                """Generuje zapytanie umorzliwające selekcje po wybranych tagach"""
                query=  f'''WITH filtered_tags AS (
                SELECT et.email_id, t.tag_name
                FROM email_tags et
                JOIN tags t ON et.tag_id = t.id
                WHERE t.tag_name IN {filters['tag']}
                )
                SELECT e.id,e.date, e.sender_email, e.recipients, e.subject , e.body,
                    GROUP_CONCAT(a.attachment_filename) AS atach
                FROM emails e
                JOIN filtered_tags ft ON e.id = ft.email_id
                LEFT JOIN attachments a ON e.id = a.email_id
                {apply_filters(filters)}
                GROUP BY e.id
                '''
            cursor.execute(query)
        elif list is not None:
            placeholders = ", ".join(["?"] * len(list))
            query=f"""
            SELECT e.id,e.date, e.sender_email, e.recipients, e.subject , e.body,
            GROUP_CONCAT(a.attachment_filename) AS atach
            FROM emails e
            LEFT JOIN attachments a ON e.id = a.email_id
            WHERE e.id in ({placeholders})
            GROUP BY e.id
            """
            cursor.execute(query,list)
        
        
        results = cursor.fetchall()
        
        #print(results)
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
        #print(query)
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
        #print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizowania tagów: {e}")
            print(f"Błąd podczas aktualizowania tagów: {e}")


def delate_label(db_connection,id_tag):
    """Usuwa labelke o wskazanym id"""
    try:
        query = f""" 
        DELETE FROM labels_name WHERE id = {id_tag} 
        """
        #print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        #print("")
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas usuwania labelki z tabeli labels_name: {e}")
            print(f"Błąd podczas usuwania labelki z tabeli labels_name: {e}")

def updata_label_name(db_connection,id_tag,new_tag_name):
    """Uaktualnia nazwę wskazanej labelki"""
    try:
        query = f"""
        UPDATE labels_name set label_name = '{new_tag_name}' WHERE ID = {id_tag}
        """
        
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizowania labelek: {e}")
            print(f"Błąd podczas aktualizowania labelek: {e}")

def select_all_label(db_connection):
    '''Pobiera wszystkie labelki z danej skrzynki odbiorczej'''
    try:
        query = f"""
        SELECT 
        email_labels.id,
        email_labels.label,
        labels_name.label_name,
        email_labels.id_email
        FROM email_labels
        JOIN labels_name ON email_labels.id_labels_name = labels_name.id;
    """ 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results 
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania wszystkich labelek: {e}")
            print(f"Błąd podczas pobierania wszystkich labelek: {e}")


def get_all_attachment(db_connection):
    '''Pobiera wszystkie labelki z danej skrzynki odbiorczej'''
    try:
        query = f"""
        SELECT * from attachments 
    """ 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results 
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania wszystkich zalacznikow: {e}")
            print(f"Błąd podczas pobierania wszystkich zalacznikow: {e}")

def get_all_recipients_by_group(db_connection):
    '''Pobiera wszystkie labelki z danej skrzynki odbiorczej'''
    try:
        query = f"""
        SELECT recipients from emails
        GROUP by  recipients
    """ 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results 
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania pogrupowanych odbiorców: {e}")
            print(f"Błąd podczas pobierania pogrupowanych odbiorców: {e}")

def get_count_email(db_connection):
    '''Pobiera wszystkie labelki z danej skrzynki odbiorczej'''
    try:
        query = f"""
        SELECT count() from emails
    """ 
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results 
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas pobierania liczby emaili: {e}")
            print(f"Błąd podczas pobierania liczby emaili: {e}")

def delate_email_labels(db_connection, id_email_labels):
    """Usuwa email_labels o wskazanym id"""
    try:
        query = f""" 
        DELETE FROM email_labels WHERE id = {id_email_labels} 
        """
        #print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas usuwania labelki z tabeli labels_name: {e}")
            print(f"Błąd podczas usuwania labelki z tabeli labels_name: {e}")

def update_id_labels_name(db_connection,id_labels, id_labels_name):
    """Zmienia id_labels_name w tabeli email_labels"""
    try:
        query = f""" 
        UPDATE email_labels set id_labels_name = {id_labels_name}  WHERE ID = {id_labels}
        """
        #print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas uaktualnania labelki z tabeli labels_name: {e}")
            print(f"Błąd podczas uaktualnania labelki z tabeli labels_name: {e}")

def updata_label(db_connection,id_label,new_lebel_text):
    """Uaktualnia nazwę wskazanej labelki"""
    try:
        query = f"""
        UPDATE email_labels set label = '{new_lebel_text}' WHERE ID = {id_label}
        """
        
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
            logger.error(f"Błąd podczas aktualizowania labelek: {e}")
            print(f"Błąd podczas aktualizowania labelek: {e}")

def get_best_recipients(db_connection,name,email,sort_by):
    """10 najczęstrzych odbiorców/nadawców
        sort_by = 1 -> po ilości wysłanych
        sort_by = 0 -> po ilości odebranych
    """
    query_part = ""
    if sort_by == 0:
        query_part = "received_count"
    else:
        query_part = "sent_count"


    try:
        query=f"""
            WITH received AS (
        SELECT 
            recipients AS email,
            COUNT(*) AS received_count
        FROM emails
        WHERE 
            (sender_name LIKE '{name}' OR sender_email LIKE '{email}')
            AND (recipients NOT LIKE '{name}' AND recipients NOT LIKE '{email}')
        GROUP BY recipients
    ),
    sent AS (
        SELECT 
            sender_email AS email,
            COUNT(*) AS sent_count
        FROM emails
        WHERE 
            sender_name NOT LIKE '{name}' AND sender_email NOT LIKE '{email}'
        GROUP BY sender_email
    )
    SELECT 
        COALESCE(r.email, s.email) AS email,
        COALESCE(received_count, 0) AS received_count,
        COALESCE(sent_count, 0) AS sent_count
    FROM received r
    FULL OUTER JOIN sent s ON r.email = s.email
    ORDER BY {query_part} DESC
    LIMIT 5
    ;
        """
        # SELECT recipients, COUNT(*) AS message_count
        # FROM emails
		# where sender_name Like 'Krzysztof Wnuk' or sender_email like 'kwnuk@robertpabich.eu'
        # GROUP BY recipients
        # ORDER BY message_count DESC
        # limit 10;
        # Wyłsane 
        # SELECT recipients, COUNT(*) AS message_count
        # FROM emails
		# where (sender_name Like '{name}' or sender_email like '{email}') and (recipients not like '{name}' and recipients not like 'email' )
        # GROUP BY recipients
        # ORDER BY message_count DESC
        # limit 10;

        #odebrane 

        # SELECT sender_email, COUNT(*) AS message_count
        # FROM emails
		# where (sender_name not Like 'Krzysztof Wnuk' or sender_email not like 'kwnuk@robertpabich.eu')
        # GROUP BY sender_email
        # ORDER BY message_count DESC
        # limit 10;

        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania 10 najczestrzych odbiorcow: {e}")
        print(f"Błąd podczas pobierania 10 najczestrzych odbiorcow: {e}")
def get_propaply_email_owner_data(db_connection):
    """pobiera dane potencjalnego właściciela skrzyneki email"""
    try:
        query="""
        SELECT sender_email,sender_email FROM emails WHERE folder_id LIKE
        (SELECT id FROM folders WHERE path LIKE '%SENT' COLLATE NOCASE) limit 1
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania potencjalnego wlascicela skrzynki: {e}")
        print(f"Błąd podczas pobierania potencjalnego wlascicela skrzynki: {e}")

def get_folder_path(db_connection,dir_id):
    """pobiera sciezke folderu o wskazanym id"""
    try:
        query=f"""
        SELECT path from folders where id like '{dir_id}'
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania sciezki do kolderu o wskazanym id: {e}")
        print(f"Błąd podczas pobierania sciezki do kolderu o wskazanym id {e}")

def get_grup_data(db_connection):
    """Zwraca pogrupowane dat"""
    try:
        query="""
        SELECT DATE(date) AS date_only, COUNT(*) AS message_count
        FROM emails
        GROUP BY date_only
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania pogrupowanych dat: {e}")
        print(f"Błąd podczas pobierania pogrupowanych dat: {e}")

def get_part_query(string):
    return re.findall(r'\[([^\]]+)\]', string)

def get_operators_summary(string):
    return re.findall(r'\s(or|and)\s', string,re.IGNORECASE)

def get_operators(string):
    operators_in_case = []
    for part in string:
        operators_in_case.append(re.findall(r'\((or|and)\)', part,re.IGNORECASE))
    return operators_in_case

def get_it_tags(name_tag,db_connection):
    """Zwraca id wskazanego tagu"""
    try:
        
        query=f"""
        SELECT * 
        FROM tags
        WHERE tag_name LIKE '{name_tag}'
        """
        print(query)
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania id wybranego tagu: {e}")
        print(f"Błąd podczas pobierania id wybranego tagu {e}")

def multi_insert_tag(list,db_connection):
    try:
        print(list)
        query=f"""INSERT OR IGNORE INTO email_tags (tag_id,email_id)
                VALUES {list}"""
        cursor = db_connection.cursor()
        print(query)
        cursor.execute(query)
        db_connection.commit()
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas dodawania wielu tagow {e}")
        print(f"Błąd podczas dodawania wielu tagow {e}")
        
def multi_part_query(key,string):
    matches = get_part_query(string)
    if len(matches) > 0:
        operators_summary = get_operators_summary(string)
        operators_in_case = get_operators(matches)
        result = []
        for string in matches:
            parts = re.split(r'\s*\((?:or|and)\)\s*', string, flags=re.IGNORECASE)
            result.append([part.strip() for part in parts if part.strip()])
        formatted_result = []
        for sublist in result:
            formatted_sublist = [f"{key} LIKE '%{string}%' COLLATE NOCASE " for string in sublist]
            formatted_result.append(formatted_sublist)

        final_result = []
        for expressions, ops in zip(formatted_result, operators_in_case):
            new_expressions = []
            for i, expr in enumerate(expressions):
                new_expressions.append(expr)
                if i < len(ops):
                    new_expressions.append(f" {ops[i]} ")
            final_result.append("".join(new_expressions).strip())

        final_query = ""
        for i in range(len(final_result)-1):
            final_query += f"({final_result[i]}) {operators_summary[i]} "

        final_query += f"({final_result[-1]})"
        #print(final_query)
        return final_query
    #############################################    
    elif len((re.findall(r'\((or|and)\)', string,re.IGNORECASE))) > 0:
        operators_in_case = (re.findall(r'\((or|and)\)', string,re.IGNORECASE))
        result = []
        result = re.split(r'\s*\((?:or|and)\)\s*', string, flags=re.IGNORECASE)
        formatted_sublist = [f"{key} LIKE '%{string}%' COLLATE NOCASE" for string in result]
        final_query = ""
        for i in range(len(formatted_sublist)-1):
            final_query += f"{formatted_sublist[i]} {operators_in_case[i]} "
        final_query += f"{formatted_sublist[-1]}"
        #print(final_query)
        return final_query
    #############################################
    else:
     return f"{key} LIKE '%{string}%' COLLATE NOCASE"

def get_all_tags(db_connection):
    """Zwraca wszystki wartości z tabeli tags"""
    try:
        query="""
        SELECT * from tags
        """
        cursor = db_connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        logger.error(f"Błąd podczas pobierania z tabeli tags: {e}")
        print(f"Błąd podczas pobierania z tabeli tags: {e}")

def word_to_highline(string):
    
    matches = get_part_query(string)
    if len(matches) > 0:
        print(matches)
        operators_summary = get_operators_summary(string)
        operators_in_case = get_operators(matches)
        result = []
        for string in matches:
            parts = re.split(r'\s*\((?:or|and)\)\s*', string, flags=re.IGNORECASE)
            result.append([part.strip() for part in parts if part.strip()])
        formatted_result = []
        for sublist in result:
            formatted_sublist = [f"{string}" for string in sublist]
            formatted_result.append(formatted_sublist)
        flat_list = list(itertools.chain(*formatted_result))
        return flat_list
    #############################################    
    elif len((re.findall(r'\((or|and)\)', string,re.IGNORECASE))) > 0:
        result = []
        result = re.split(r'\s*\((?:or|and)\)\s*', string, flags=re.IGNORECASE)
        return result
    #############################################
    else:
        return string
    
