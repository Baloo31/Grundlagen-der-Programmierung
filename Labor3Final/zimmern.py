class Zimmer:

    def __init__(self, num, anz, preis, farbe, meerblick):
        self.__num = num
        self.__anz = anz
        self.__preis = preis
        self.__farbe = farbe
        self.__meerblick = meerblick

    def __str__(self):
        return "Zimmernummer: {} | Personen: {} | Preis: {} |" \
               " Farbe: {} | Meerblick: {}".format(self.num, self.anz, self.preis, self.farbe, self.meerblick)

    def __repr__(self):
        return "Zimmernummer: {} | Personen: {} | Preis: {} |" \
               " Farbe: {} | Meerblick: {}".format(self.num, self.anz, self.preis, self.farbe, self.meerblick)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def anz(self):
        return self.__anz

    @anz.setter
    def anz(self, anz):
        self.__anz = anz

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, preis):
        self.__preis = preis

    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, farbe):
        self.__farbe = farbe

    @property
    def meerblick(self):
        return self.__meerblick

    @meerblick.setter
    def meerblick(self, meerblick):
        self.__meerblick = meerblick
