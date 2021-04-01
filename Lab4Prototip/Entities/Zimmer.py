class Zimmer:
    def __init__(self, num, anz, preis, farbe, meerblick):
        self.__num = num
        self.__anz = anz
        self.__preis = preis
        self.__farbe = farbe
        self.__meerblick = meerblick

    def __str__(self):
        return "{};{};{};{};{}".format(self.num, self.anz, self.preis, self.farbe, self.meerblick)

    def __repr__(self):
        return "{};{};{};{};{}".format(self.num, self.anz, self.preis, self.farbe, self.meerblick)

    @property
    def num(self): return self.__num

    @num.setter
    def num(self, val): self.__num = val

    @property
    def anz(self): return self.__anz

    @anz.setter
    def anz(self, val): self.__anz = val

    @property
    def preis(self): return self.__preis

    @preis.setter
    def preis(self, val): self.__preis = val

    @property
    def farbe(self): return self.__farbe

    @farbe.setter
    def farbe(self, val): self.__farbe = val

    @property
    def meerblick(self): return self.__meerblick

    @meerblick.setter
    def meerblick(self, val): self.__meerblick = val
