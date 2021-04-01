from Entities.Gast import Gast
from Entities.Zimmer import Zimmer
from Entities.Reserv import Reservierung
import datetime
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename


class Rep:
    def __init__(self, file_g, file_z, file_r):
        self.__f_name_g = file_g
        self.__f_name_z = file_z
        self.__f_name_r = file_r

    def load_from_file(self, hotel):
        # Deschiderea fisierului de oaspeti pentru a citi
        file_g = open(self.__f_name_g, "r")
        # Extragerea datelor din acest fisier si salvarea lor in lista de oaspeti din hotel
        for line in file_g:
            line = line.strip().split("|")
            if line[2] == "":
                hotel.gaste.append(Gast(line[0], line[1], []))
            else:
                liste = line[2].split(",")
                lr = []
                # Partea urmatoare se ocupa cu
                for el in liste:
                    res = el.split(";")
                    ci = res[2].split("-")
                    ci = datetime.date(int(ci[0]), int(ci[1]), int(ci[2]))
                    co = res[3].split("-")
                    co = datetime.date(int(co[0]), int(co[1]), int(co[2]))
                    lr.append(Reservierung(int(res[0]), int(res[1]), ci, co))
                hotel.gaste.append(Gast(line[0], line[1], lr))
        # Inchiderea fisierului
        file_g.close()

        # Deschiderea fisierului pentru camere
        file_z = open(self.__f_name_z, "r")
        # Salvarea datelor din acesta in lista de camere din hotel
        for line in file_z:
            line = line.strip().split(";")
            hotel.zimmern.append(Zimmer(int(line[0]), int(line[1]), int(line[2]), line[3], bool(line[4])))
        # Inchiderea fisierului
        file_z.close()

        # Deschiderea fisierului pentru rezervari
        file_r = open(self.__f_name_r, "r")
        # Salvarea datelor in lista de rezervari (ele sunt aceleasi cu cele din listele de
        # rezervari ale fiecarui oaspete)
        for line in file_r:
            line = line.strip().split(";")
            ci = line[2].strip().split("-")
            co = line[3].strip().split("-")
            hotel.reservierungen.append(Reservierung(int(line[0]), int(line[1]), datetime.date(int(ci[0]),
                                        int(ci[1]), int(ci[2])), datetime.date(int(co[0]),
                                                                               int(co[1]), int(co[2]))))
        # Inchiderea fisierului
        file_r.close()

    def store_to_file(self, hotel):
        # Deschidem fisierul de oaspeti pentru rescrierea lui
        file_g = open(self.__f_name_g, "w")
        # Datele din lista de oaspeti a hotelului sunt scrise in fisier
        for el in hotel.gaste:
            lr_str = ""
            for res in el.lr:
                lr_str += str(res)
                if res != el.lr[-1]:
                    lr_str += ", "
            file_g.write("{}|{}|{}\n".format(el.vorname, el.nachname, lr_str))
        # Inchiderea fisierului
        file_g.close()

        # Deschidem fisierul de camere pentru rescrierea lui
        file_z = open(self.__f_name_z, "w")
        # Datele din lista de camere a hotelului sunt scrise in fisier
        for el in hotel.zimmern:
            if not el.meerblick:
                el.meerblick = ""
            file_z.write("{};{};{};{};{}\n".format(el.num, el.anz, el.preis, el.farbe, el.meerblick))
        # Inchiderea fisierului
        file_z.close()

        # Deschidem fisierul de rezervari pentru rescrierea lui
        file_r = open(self.__f_name_r, "w")
        # Datele din lista de rezervari a hotelului sunt scrise in fisier
        for el in hotel.reservierungen:
            file_r.write("{};{};{};{}\n".format(el.zimmer, el.nrg, el.ci, el.co))
        # Inchiderea fisierului
        file_r.close()


"""
def search_and_load(hotel):
    x = Tk()
    x.withdraw()
    datei = askopenfilename(title="Bitte wahlen sie eine Datei !", filetype=(("Text files", ".txt"),
                                                                             ("All files", ".*")))
    x.destroy()
    if datei:
        rep = Rep(datei)  # Hier bekommt man die Daten des ausgewahltes Datei
        rep.load_from_file(hotel)
"""
