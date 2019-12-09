# -*- coding: utf-8 -*-
# Berechnung der Primfaktoren einer Zahl in einer Liste
from typing import List

loop = True
while loop:
    # Eingabe
    input_number : int = int(input("Bitte Nummer eingeben: "))
    number : int = input_number

    # Verarbeitung
    factors : List[int] = []    # Liste zum Sammeln der Faktoren
    divider : int = 2
    while number > 1:
        while number % divider == 0:
            factors.append(divider)
            number //= divider # number = number // divider (integer division)
        divider = divider + 1

    # Ausgabe
    print("{:s} = {:d}".format(" ⋅ ".join(map(str, factors)), input_number))

    if input("Noch einmal ausführen (J/N)? ") not in "JjYy":
        loop = False
