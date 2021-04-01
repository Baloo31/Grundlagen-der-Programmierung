from Entitati.Submarin import Submarin


class Pre:
    def __init__(self, datei, data):
        self.datei = datei
        self.data = data

    def load_from_file(self):
        # Deschidere fisier
        file = open(self.datei, "r")

        # Extragere date
        for line in file:
            t = line.strip().split(", ")
            # Aici se petrece validarea datelor
            if int(t[0]) in range(1, 12) and int(t[1]) <= int(t[0]) and int(t[1]) >= 0:
                self.data.append(Submarin(int(t[0]), int(t[1]), int(t[2]), int(t[3])))
        # Inchidere fisier
        file.close()
