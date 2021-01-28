# Demonstration von Properties

class MyClassVanilla:
    """ Klasse mit einfachem Attribut (ohne Propertie) """

    def __init__(self):
        self.value = 0


class MyClassProperties:
    """ Klasse mit Propertie, das im Setter überprüft wird.
        Entscheidendes Kriterium: Eine nachträgliche Abstraktion
        durch Datenkapselung (Geheimnisprinzip) ist ohne
        Veränderung der Schnittstelle möglich.
    """

    def __init__(self):
        self.value = 0

    @property
    def value(self):
        return self.__value  # stark privat durch __ am Anfang
        # (vgl. https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles)

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("value parameter must not be <0")
        else:
            self.__value = value


# Vanilla ohne Properties
oop = MyClassVanilla()
print(oop.value)
oop.value = 1
print(oop.value)
oop.value = -1
print(oop.value)

# mit Properties und Wertekontrolle
try:
    omp = MyClassProperties()
    print(omp.value)
    omp.value = 1
    print(omp.value)
    omp.value = -1  # Bang!
    print(omp.value)
except ValueError as e:
    print(f"Error: {e}")
