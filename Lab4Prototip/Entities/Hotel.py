class Hotel:
    def __init__(self):
        self.__gaste = []
        self.__zimmern = []
        self.__reservierungen = []

    def __str__(self):
        return f'{self.gaste} ||| {self.zimmern} ||| {self.reservierungen}'

    @property
    def gaste(self): return self.__gaste

    @gaste.setter
    def gaste(self, val): self.__gaste = val

    @property
    def zimmern(self): return self.__zimmern

    @zimmern.setter
    def zimmern(self, val): self.__zimmern = val

    @property
    def reservierungen(self): return self.__reservierungen

    @reservierungen.setter
    def reservierungen(self, val): self.__reservierungen = val
