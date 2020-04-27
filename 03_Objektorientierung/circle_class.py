# -*- coding: utf-8 -*-
# Implementierung zur Übung

from typing import Tuple
from math import pi


class Circle:
    """ Class for circles with radius and center point """

    def __init__(self, cpoint: Tuple[float, float], radius: float):
        """ Create new circle object
        :param cpoint: centre point as tuple of x and y value
        :param radius: radius of circle
        """
        self.cpoint = cpoint
        self.radius = radius

    def get_perimeter(self) -> float:
        """ Get perimeter for circle
        :return: perimeter as float
        """
        return 2 * self.radius * pi

    def get_area(self) -> float:
        """ Get size of area of circle
        :return: area size as float
        """
        return self.radius ** 2 * pi

    def scale(self, factor: float) -> None:
        """ Scale circle by factor
        :param factor: factor to multiply radius with
        """
        self.radius *= factor

    def __str__(self):
        """ Build string for object
        :return: suitable string with values
        """
        return "Circle: ( %f | %f ), radius: %f" % (
            self.cpoint[0],
            self.cpoint[1],
            self.radius
        )


# Main Program: Demonstration of two circle objects

p1 = (1.2, 2.2)
c1 = Circle(p1, radius=1.3)
print(c1.get_perimeter())
print(c1)

p2 = (0.7, 3.2)
c2 = Circle(p2, radius=2.4)
print(c2.get_perimeter())
c2.scale(1.7)
print(c2.get_perimeter())
print("Circle 2: (", c2.cpoint[0], "|", c2.cpoint[1],
      ") radius:", c2.radius)
print(c2)
