Ein simpler Kassenrechner der alle veränderungen des Kassenwertes speichert erst in einem Log un nach beendung in einem LibreOfficecalc Dokument.
Programiert in Python, alle Libs und Bibs siond von pyhton auser odfpy die instalieren umd cmd mit " pip install odfpy " und dan habt ihr alles

Dafür habe ich ein simples Youtube Tutorial genutz um die Basis der Rechnerfunktionen zu erlangen (https://www.youtube.com/watch?v=SUNJvH4yzg4) 
Der Rest ist selbstgeschrieben.

Empfohlene Ordner Struktur: 
Projekt/
│
├── Kassenrechner.py              # Das Hauptprogramm
├── kassenstadnspeicher.txt       # Zwischen Logs
├── logs_to_ods.py                # Das neben Prgramm zum umwandeln 
└── Kassenwerte.ods               # Die Logs in der ODS Datei

Logs sehen in der .txt Datei ungefähr so aus: 
# format YYYY-MM-DD-HH-MM-SS-FF: Wert Bemerkung  
2026-02-03 22:45:06.741261: 250.0 Startwert! # Startwert der Kasse
2026-02-03 22:45:11.343949: 350.0 + Operation # Operation, hier eine Addition
2026-02-03 22:45:24.310398: 294.0 - Operation # Operation, hier eine Subtraktion
2026-02-03 22:45:37.467063: 297.5 + Operation # Operation, Addition
2026-02-03 22:45:40.474798: 297.5 Endwert # Endwert der Kasse 
