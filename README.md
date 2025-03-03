# Witam w  Firenet Viewer

**Opis:**

Po skolonowaniu środowiska:
1. python3 -m venv "nazwa_wrirtualnego środowiska" -> tworzenie wirtualengo środowiska
2. source venv/bin/activate -> aktywajcja wirtualnego środowiska
3. pip3 install -r requirements.txt -> installacja potrzebnych paczek
4. python3 create_database.py -> tworzenie nowej bazy danych.
5. python3 main.py -> otworzenie GUI 
6. pip install --upgrade pip setuptools wheel -> problemy z outdated wheel

Monitorowanie zmienianych komponentów z QT do GUI:
 * Custom_Widgets --monitor-ui ui

Wykonanie exec file: 
* pyinstaller main.spec

**TODO:**
1. Add ToolTips to a project for every button in the navbar

**PROBLEMS WITH PYTHON 3.12?**
https://stackoverflow.com/questions/77364550/attributeerror-module-pkgutil-has-no-attribute-impimporter-did-you-mean

**OR**
python3.11 -m venv venv -> tworzenie środowiska z python 3.11
source venv3.11/bin/activate -> włączenie środowiska z python 3.11
