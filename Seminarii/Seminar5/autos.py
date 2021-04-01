class AutoBox:
    def __init__(self):
        self.autos = []

    def add_auto(self, auto):
        self.autos.append(auto)

    def get_autos(self):
        return self.autos

    def sum_ver(self):
        sum = 0
        for auto in self.autos:
            if auto.get_modus() == "Sport":
                sum += auto.get_verbrauch()
        return sum

    def durchschnittsverbrauch(self):
        sum = 0
        for auto in self.autos:
            sum += auto.get_verbrauch()
        return sum/len(self.autos)

    def remove_cars(self):
        avg = self.durchschnittsverbrauch()
        i = 0
        for auto in self.autos:
            if auto.get_verbrauch() > avg:
                self.autos.pop(i)
                i -= 1
            i += 1
