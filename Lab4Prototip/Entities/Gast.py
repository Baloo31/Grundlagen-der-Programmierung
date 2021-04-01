class Gast:
    def __init__(self, vorname, nachname, lr):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__lr = lr

    def __str__(self):
        return "{}|{}|{}".format(self.vorname, self.nachname, self.lr)

    def __repr__(self):
        return "{}|{}|{}".format(self.vorname, self.nachname, self.lr)

    @property
    def vorname(self): return self.__vorname

    @vorname.setter
    def vorname(self, vorname): self.__vorname = vorname

    @property
    def nachname(self): return self.__nachname

    @nachname.setter
    def nachname(self, nachname): self.__nachname = nachname

    @property
    def lr(self): return self.__lr

    @lr.setter
    def lr(self, lr): self.__lr = lr
