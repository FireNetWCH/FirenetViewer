import sqlite3, os
from datetime import datetime
import pytz



def update_hours(db_path):
    # Połączenie z bazą
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Strefy czasowe
    utc = pytz.utc
    poland = pytz.timezone('Europe/Warsaw')

    # Pobierz wszystkie rekordy
    cursor.execute("SELECT id, date FROM emails")
    rows = cursor.fetchall()

    # Przetwórz i zaktualizuj daty
    for row in rows:
        id_, date_str = row
        try:
            # Parsujemy datę jako UTC
            dt_utc = utc.localize(datetime.fromisoformat(date_str))

            # Konwertujemy na czas polski (uwzględnia czas letni/zimowy)
            dt_poland = dt_utc.astimezone(poland)

            # Zapisujemy nową wartość jako string w ISO
            new_date_str = dt_poland.strftime('%Y-%m-%d %H:%M:%S')

            # Aktualizacja w bazie
            cursor.execute("UPDATE emails SET date = ? WHERE id = ?", (new_date_str, id_))
        except Exception as e:
            print(f"Błąd przy id={id_}: {e}")

    # Zatwierdź i zamknij
    conn.commit()
    conn.close()


if __name__=="__main__":

    examined_dir = "E:\\sqlite_with_headers 3.0" #"E:\\sqlite_with_headers 2.0"

    for root,dirs,files in os.walk(examined_dir):
        for file in files:
            if file.endswith(".sqlite"):
                db_path = os.path.join(root, file)
                update_hours(db_path)
                print(f"Pomyślnie zaktualizowano daty w pliku: {db_path}")
