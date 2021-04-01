class Rational:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "{}/{}".format(self.x, self.y)

    def add(self, o):
        return Rational(self.x * o.y + o.x * self.y, self.y * o.y)

    def sub(self, o):
        return Rational(self.x * o.y - o.x * self.y, self.y * o.y)

    def mul(self, o):
        return Rational(self.x * o.x, self.y * o.y)

    def div(self, o):
        return Rational(self.x * o.y, self.y * o.x)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
