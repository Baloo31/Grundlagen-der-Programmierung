class Auto:

    def __init__(self, modell, farbe, baujahr):
        self.__modell = modell
        self.__farbe = farbe
        self.__baujahr = baujahr

    def __str__(self):
        return "{}/{}/{}".format(self.modell, self.farbe, self.baujahr)

    def __repr__(self):
        return "{}/{}/{}".format(self.modell, self.farbe, self.baujahr)

    def tanken(self):
        print('tanken')

    def anlassen(self):
        print('anlassen')

    @property
    def modell(self):
        return self.__modell

    @modell.setter
    def modell(self, modell):
        self.__modell = modell

    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, farbe):
        self.__farbe = farbe

    @property
    def baujahr(self):
        return self.__baujahr

    @baujahr.setter
    def baujahr(self, baujahr):
        self.__baujahr = baujahr
