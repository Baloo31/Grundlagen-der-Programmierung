class Raum:
    def __init__(self, raumnummer, anz_s):
        self.raumnummer = raumnummer
        self.anz_s = anz_s

    @property
    def raumnummer(self):
        return self.__raumnummer

    @raumnummer.setter
    def raumnummer(self, raumnummer):
        self.__raumnummer = raumnummer

    @property
    def anz_s(self):
        return self.__anz_s

    @anz_s.setter
    def anz_s(self, anz_s):
        self.__anz_s = anz_s

    def __eq__(self, o):
        return self.raumnummer == o.raumnummer and self.anz_s == o.anz_s

    def __str__(self):
        return "{},{}".format(self.__raumnummer, self.anz_s)
