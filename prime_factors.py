# Berechnung der Primfaktoren einer Zahl in einer Liste

loop = True
while loop:
    # Eingabe
    number = input_number = int(input("Bitte Nummer eingeben: "))

    # Verarbeitung
    factors = []    # Liste zum Sammeln der Faktoren
    divider = 2
    while number > 1:
        while number % divider == 0:
            factors.append(divider)
            number //= divider
        divider = divider + 1
        if divider * divider > number:
            if number > 1: factors.append(number)
            break # Zeit sparen, denn Teiler zu groß wird

    # Ausgabe
    print("{:s} = {:d}".format(" ⋅ ".join(map(str, factors)), input_number))

    # Potenzen bestimmen
    bases = []      # Liste zum Sammeln der Basiswerte
    exponents = []  # Liste zum Sammeln und Zählen der Exponenten
    index = 0
    while index < len(factors): # alle Faktoren bearbeiten
        if len(bases) > 0 and bases[-1] == factors[index]: # Basis schon vorhanden
            exponents[-1] += 1
        else: # Basis ist neu
            # mit Exponent 1 hinzufügen
            bases.append(factors[index])
            exponents.append(1)
        index += 1

    # Ausgabe
    print()
    # Exponenten
    print((3*" ").join([(len(str(b)) + 1) * " " + str(e) for b, e in zip(bases, exponents)]))
    # Basiswerte und Ergebnis
    print("{:s} = {:d}".format(" ⋅ ".join([str(b) + " " * (len(str(e)) + 1 )
                                           for b, e in zip(bases, exponents)]), input_number))

    if input("Noch einmal ausführen (J/N)? ") not in "JjYy":
        loop = False