class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __str__(self):
        return "{}/{}".format(self.x, self.y)

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
