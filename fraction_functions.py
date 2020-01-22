# Funktionen fuer Brueche in Tupeln (Uebungsaufgabe)

def printFract(fraction):
   print(fraction[0]) # Zaehler ausgeben
   print("---------")
   print(fraction[1]) # Nenner ausgeben

def negFract(fraction):
   result = (-fraction[0], fraction[1])
   return result

def inputFract():
   numerator = input("Bitte Zaehler eingeben: ")
   denominator = input("Bitte Nenner eingeben: ")
   return (int(numerator), int(denominator))


# Hauptprogramm
b = inputFract()
printFract(b)
print()
printFract(negFract(b))