class Kunde:

    def __init__(self, name, betrag):
        self.__name = name
        self.__betrag = betrag

    def __str__(self):
        return "{}/{}".format(self.name, self.betrag)

    def __repr__(self):
        return "{}/{}".format(self.name, self.betrag)

    def verdienen(self, gehalt):
        self.__betrag += gehalt

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def betrag(self):
        return self.__betrag

    @betrag.setter
    def betrag(self, betrag):
        self.__betrag = betrag
