class Auto:
    def __init__(self, farbe, modus, verbrauch, marke):
        self.farbe = farbe
        self.modus = modus
        self.verbrauch = verbrauch
        self.marke = marke
  
    def get_farbe(self):
        return self.farbe

    def get_modus(self):
        return self.modus

    def get_verbrauch(self):
        if self.modus == "Sport":
            return self.verbrauch * 1.5
        elif self.modus == "Eco":
            return self.verbrauch * 0.7
        else:
            return self.verbrauch

    def get_marke(self):
        return self.marke

    def __str__(self):
        return "Auto %s mit Farbe %s und Modus %s hat %s" % (self.marke, self.farbe, self.modus, self.verbrauch)
