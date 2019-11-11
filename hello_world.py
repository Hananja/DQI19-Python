# Hello World Demonstration mit verschachtelten Verzweigungen
# DQI19 am 02. Oktober 2019

# Eingabe
firstname : str = input("Bitte Vorname eingeben: ")
lastname : str = input("Bitte Nachname eingeben: ")
sex : str = input("Bitte Geschlecht (m/w) eingeben: ")

# Verarbeitung
if lastname == "":
    greeting = "Hallo " + firstname
else:
    if not sex == "m":
        greeting = "Guten Morgen Frau " + lastname
    else:
        greeting = "Guten Morgen Herr " + lastname

# Ausgabe
print(greeting)
