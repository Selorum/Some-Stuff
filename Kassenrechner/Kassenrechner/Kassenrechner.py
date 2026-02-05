from datetime import datetime
from logs_to_ods import export_logs_to_ods

# speicherwert
kassenstand_speicher = []


# Initialisierung des Kassenstandes und speicherung
kassenstand = float(input("kassenstand in Euros?  "))
kassenstand_speicher.append(f"{datetime.now()}: {kassenstand}" + " Startwert!")

while(True):

    # Addition
   def einnahmen(kassenstand, b):
       return kassenstand + b
    # Subtraktion
   def ausgaben(kassenstand, b):
       return kassenstand - b

   choice = input("+ / - / Beenden(3) ")
   if (choice == "3"): # Beenden und spreichern
       print("Die Rechnung wurde beendet!")
       print("Der Kassenstand berträgt:", kassenstand, "€")
       kassenstand_speicher.append(f"{datetime.now()}: {kassenstand}" + " Endwert")
       break
   num1 = float(input("Zahl eingeben:  ")) # Eingeben des Summandens

   if (choice == "+"): # Addition
       print(kassenstand,"€", "+", num1,"€")
       print("Kassenstand =", einnahmen(kassenstand, num1), "€")
       kassenstand = kassenstand + num1
       kassenstand_speicher.append(f"{datetime.now()}: {kassenstand}" + " + Operation")
   elif (choice == "-"): # Subtraktion
       print(kassenstand, "€", "-", num1, "€")
       print("Kassenstand", ausgaben(kassenstand, num1), "€")
       kassenstand = kassenstand - num1
       kassenstand_speicher.append(f"{datetime.now()}: {kassenstand}" + " - Operation")
   else: # sichrung damit keien Falschen eingabne getätigt werden können
       print("Falsche Eingabe!")

with open("kassenstandspeicher.txt", "w") as file: # Speichern des gesamten ablaufes
    for entry in kassenstand_speicher:
        file.write(entry + "\n")

# speichern als ods datei für bessere lesbarkeit
## export_logs_to_ods("kassenstandspeicher.txt")