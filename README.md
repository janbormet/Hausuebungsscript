# Hausuebungsscript
- Python script, welches das importieren der Java-Hausübungen erleichtert und die testbenches überall einfügt

1.) Script runterladen
2.) Im moodle alle Abgaben Auswählen, gabz unten Hanken setzen bei "Abgaben in Verzeichnissen herunterladen"!!! und dann unten "Ausgewählte Abgaben herunterladen"
3.) Irgendwo einen LEEREN Ordner erstellen, in welchem die Abgaben später landen
4.) Tutor Test(s) herunterladen 
5.) Script starten mit   python3 huscript.py
6.) Zip-file aus 2.) im Dateimanagerprompt auswählen
7.) Zielordner aus 3.) im Dateimanagerprompt auswählen
8.) nacheinander alle Testbenches auswählen, (nach der letzten Testbench einfach den prompt schließen)
9.) In eclipse: import -> Existing Projects into Workspace -> Select root directory -> Browse -> Ordner aus 3.) Wählen -> Finish

Ich konnte noch nicht testen, wie es funktioniert, wenn in der Vorlage mehrere Packages definiert sind etc. Falls es dann probleme geben sollte einfach vorher in die jeweiligen Testbenches oben einfügen import packagename.*; dann sollte es keine Probleme geben.

-Python3 verwenden
-getestet auf Windows 10 und Linux (open-suse Leap 15.1)
