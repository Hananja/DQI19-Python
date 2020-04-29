from __future__ import annotations

FRACTION_BAR_WIDTH = 5

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
        pass # TODO

    # cancel ... TODO


# Hauptprogramm
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

for f in f1, f2:
    f.print()
