# Witam w  Firenet Viewer

**Opis:**

Po skolonowaniu środowiska:
1. python3 -m venv "nazwa_wrirtualnego środowiska" -> tworzenie wirtualengo środowiska
2. source venv/bin/activate -> aktywajcja wirtualnego środowiska
3. pip3 install -r requirements.txt -> installacja potrzebnych paczek
# dla condy dodatkowo conda install -c conda-forge pycairo
4. python3 create_database.py -> tworzenie nowej bazy danych.
5. python3 main.py -> otworzenie GUI 

Monitorowanie zmienianych komponentów z QT do GUI:
 * Custom_Widgets --monitor-ui ui

Wykonanie exec file: 
* pyinstaller main.spec
* set PYDEVD_DISABLE_FILE_VALIDATION=1

**TODO:**
1. Add ToolTips to a project for every button in the navbar
