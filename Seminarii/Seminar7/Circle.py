import math


class Circle:
    def __init__(self, mitte, radius):
        self.__mitte = mitte
        self.__radius = radius

    def __mul__(self, o):
        return Circle(self.mitte + o.mitte, self.radius * o.radius)

    def __str__(self):
        return "( {} ; {} )".format(self.mitte, self.radius)

    def compute_area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{}.{}".format(self.mitte, self.radius)

    def __eq__(self, other):
        return self.__mitte == other.mitte and self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @property
    def mitte(self):
        return self.__mitte

    @mitte.setter
    def mitte(self, mitte):
        self.__mitte = mitte

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
