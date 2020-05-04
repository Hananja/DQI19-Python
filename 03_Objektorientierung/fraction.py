from __future__ import annotations

FRACTION_BAR_WIDTH = 5


def gcd(a, b):
    while b != 0:
        h = a % b
        a = b
        b = h
    return a

class Fraction:
    # Konstruktor: automatisch aufgerufen bei Objekterzeugung
    def __init__(self, numerator: int, denominatior: int):
        self.numerator : int = numerator
        self.denominator : int = denominatior

    def print(self) -> None:
       print()
       print(self.numerator)
       print(FRACTION_BAR_WIDTH * "-")
       print(self.denominator)
       print()

    def add(self, other: Fraction):
        self.numerator = self.numerator * other.denominator + \
            self.denominator * other.numerator
        self.denominator = self.denominator * other.denominator
        self.cancel()

    def cancel(self):
        gcd_val = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // gcd_val
        self.denominator = self.denominator // gcd_val

    def input_console(self):
        numerator = input("Bitte Zaehler eingeben: ")
        denominator = input('Bitte Nenner eineben: ')
        # TODO: Error Handling
        self.numerator = int(numerator)
        self.denominator = int(denominator)


# Fabrikfunktion
def inputFract():
    numerator = input("Bitte Zaehler eingeben: ")
    denominator = input('Bitte Nenner eineben: ')
    # TODO: Error Handling
    return Fraction(int(numerator), int(denominator))


# Hauptprogramm
f1 = inputFract()
f2 = Fraction(3, 4)

for f in f1, f2:
    f.print()

f1.add(f2)
f1.print()

f1.input_console()
f1.print()