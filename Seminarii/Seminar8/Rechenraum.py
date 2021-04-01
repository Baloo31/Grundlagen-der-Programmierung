from Raum import Raum


class Rechenraum(Raum):
    def __init__(self, so, raumnummer, anz_s):
        if so not in ["Linux", "Windows", "Unix", "MacOS"]:
            raise ValueError()
        Raum.__init__(self, raumnummer, anz_s)
        self.so = so

    def __str__(self):
        return "{} ; {} ; {}".format( self.so, self.raumnummer, self.anz_s)

    @property
    def so(self):
        return self.__so

    @so.setter
    def so(self, so):
        self.__so = so
