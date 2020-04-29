# Funktionen fuer Brueche in Tupeln (Uebungsaufgabe)
from typing import Tuple


def printFract(fraction: Tuple[float, float]) -> None:
    """ Print a fraction out to console.
    :param fraction: fraction as tuple of number
    :type fraction: fraction as tuple of numerator and denominator
    :return: nothing
    :rtype: NoneType
    """
    print()
    print(fraction[0])
    print("------")
    print(fraction[1])
    print()


def negFract(fraction):
    result = (-fraction[0], fraction[1])
    return result


def inputFract():
    numerator = input("Bitte Zaehler eingeben: ")
    denominator = input('Bitte Nenner eineben: ')
    return (int(numerator), int(denominator))


def gcd(a, b):
    while b != 0:
        h = a % b
        a = b
        b = h
    return a


def cancelFract(fraction):
    gcd_val = gcd(fraction[0], fraction[1])
    return (fraction[0] / gcd_val, fraction[1] / gcd_val)


def invFract(fraction):
    inverted = (fraction[1], fraction[0])
    return inverted


def addFract(fraction, fraction2):
    result = (fraction[0] * fraction2[1]
              + fraction[1] * fraction2[0],
              fraction[1] * fraction2[1])
    return cancelFract(result)


def subFract(fraction, fraction2):
    return addFract(fraction, negFract(fraction2))


def mulFract(fraction, fraction2):
    result = (fraction[0] * fraction2[0],
              fraction2[1] * fraction[1])
    return cancelFract(result)


def divFract(fraction, fraction2):
    return mulFract(fraction, invFract(fraction2))


# hauptprogramm
b = inputFract()
printFract(b)
print()
printFract(negFract(b))
print()
printFract(invFract(b))
print()
printFract(addFract((3, 4), (2, 7)))
printFract(subFract((3, 4), (2, 7)))
printFract(mulFract((3, 4), (2, 7)))
printFract(divFract((3, 4), (2, 7)))
print(gcd(2, 4))
printFract(cancelFract((20, 100)))

print(printFract.__doc__)
