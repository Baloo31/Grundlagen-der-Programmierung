class Autohaus:

    def __init__(self):
        self.__autos = []
        self.__solds = []

    @property
    def autos(self):
        return self.__autos

    @property
    def solds(self):
        return self.__solds

    def add_auto(self, auto):
        self.__autos.append(auto)

    def sell_auto(self, auto, kunde):
        self.__autos.pop(self.__autos.index(auto))
        self.__solds.append((auto, kunde))
