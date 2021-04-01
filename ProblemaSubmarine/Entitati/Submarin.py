class Submarin:
    def __init__(self, cabine, incinte_inundate, x, y):
        self.__lista_cabine = cabine
        self.__incinte_inundate = incinte_inundate
        self.__nr_marinari = 0
        self.__x = x
        self.__y = y

    def __str__(self):
        return "{}/{}".format(self.__lista_cabine, self.__incinte_inundate)

    def __repr__(self):
        return "{}/{}".format(self.__lista_cabine, self.__incinte_inundate)

    def raporteaza_situatie(self, cheie_criptare):
        # Cheia de criptare poate fi o valoare negativa
        return "{}{}".format(abs(self.__nr_marinari + cheie_criptare), abs(self.__incinte_inundate + cheie_criptare))

    @property
    def lista_cabine(self):
        return self.__lista_cabine

    @lista_cabine.setter
    def lista_cabine(self, lista_cabine):
        self.lista_cabine = lista_cabine

    @property
    def incinte_inundate(self):
        return self.__incinte_inundate

    @incinte_inundate.setter
    def incinte_inundate(self, incinte_inundate):
        self.__incinte_inundate = incinte_inundate

    @property
    def nr_marinari(self):
        return self.__nr_marinari

    @nr_marinari.setter
    def nr_marinari(self, nr_marinari):
        self.__nr_marinari = nr_marinari

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
