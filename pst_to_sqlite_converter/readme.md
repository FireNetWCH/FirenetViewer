# Instrukcja uruchamiania skryptów backendowych do konwersji pst na sqlite 

## 1. pst_to_sqlite.py - Przetworzenie kontenerów PST

W pierwszej kolejności należy przetworzyć pliki .pst na pliki .sqlite z wyrzuconymi obok załącznikami - w zależności od potrzeb można modelować funkcję main do danego przypadku użycia np. wyszukiwania plików .pst znajdujących się w zadanym katalogu i podkatalogach (domyślnie jest po prostu podanie w formie listy plików znajdujących się w danym katalogu).

## 2. sqlite_postprocessor.py - Poprawienie i dodanie dodatkowych danych w bazach SQLITE

Następnym wymaganym krokiem jest dodatkowe przeprocesowanie otrzymanych w wyniku działania pierwszego skryptu plików .sqlite.

## 3. update_hours.py - Dostosowanie godzin do polskiej strefy czasowej 

Krok opcjonalny. Skrypt poprawia niepoprawne stemple czasu na czas polski.
