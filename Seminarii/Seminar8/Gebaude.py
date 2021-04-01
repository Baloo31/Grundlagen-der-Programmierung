class Gebaude:
    def __init__(self, raumen, nume):
        self.raumen = raumen

    def wievielplatz(self, raum, nume):
        for r in self.raumen:
            if raum == r.raumnummer:
                return r.anz_s

    def __str__(self):
        return


    @property
    def raumen(self):
        return self.__raumen

    @raumen.setter
    def raumen(self, val):
        self.__raumen = val

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, val):
        self.__nume = val

