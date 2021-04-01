from GUI.gaste import *
from GUI.zimmern import *
from GUI.reservierungen import *


class First:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Gaste Menu')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)  # Aici avem meniul oaspeti si functionalitatile sale

        self.button_one = tk.Button(self.top,  text='Zuruck', command=self.close)
        self.button_one.pack(fill=tk.BOTH)

        self.button_two = tk.Button(self.top,  text='Füge ein neuer Gast hin', command=self.add_guest)
        self.button_two.pack(fill=tk.BOTH)

        self.button_three = tk.Button(self.top, text='Aktualisierung der Nachname eines Gastes', command=self.update)
        self.button_three.pack(fill=tk.BOTH)

        self.button_four = tk.Button(self.top, text='Löschung eines Gastes', command=self.delete_guest)
        self.button_four.pack(fill=tk.BOTH)

        self.button_five = tk.Button(self.top, text='Anzeige die Liste von Gästen', command=self.anzeige)
        self.button_five.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def add_guest(self):
        self.add = tk.Toplevel(self.root)
        self.add_g = Add_Guest(self.add, self.hotel)

    def update(self):
        self.update = tk.Toplevel(self.root)
        self.update_guest = Update_Guest(self.update, self.hotel)

    def delete_guest(self):
        self.delete = tk.Toplevel(self.root)
        self.delete_guest = Delete_Guest(self.delete, self.hotel)

    def anzeige(self):
        self.print = tk.Toplevel(self.root)
        self.print_guest = Print_Gast(self.print, self.hotel)


class Second:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Zimmer Menu')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root) # Aici avem meniul camere si functionalitatile sale

        self.button_one = tk.Button(self.top,  text='Zuruck', command=self.close)
        self.button_one.pack(fill=tk.BOTH)

        self.button_two = tk.Button(self.top,  text='Füge ein Zimmer hin', command=self.add_zimmer)
        self.button_two.pack(fill=tk.BOTH)

        self.button_three = tk.Button(self.top, text='Aktualisierung des Preises eines Zimmers', command=self.akt_preis)
        self.button_three.pack(fill=tk.BOTH)

        self.button_four = tk.Button(self.top, text='Löschung eines Zimmers', command=self.delete)
        self.button_four.pack(fill=tk.BOTH)

        self.button_five = tk.Button(self.top, text='Anzeige die Liste von Zimmern', command=self.anzeige)
        self.button_five.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def add_zimmer(self):
        self.zimmer = tk.Toplevel(self.root)
        self.add_z = Add_Room(self.zimmer, self.hotel)

    def akt_preis(self):
        self.preis = tk.Toplevel(self.root)
        self.update_p = Aktualisiere_Preis(self.preis, self.hotel)

    def delete(self):
        self.d = tk.Toplevel(self.root)
        self.dlt = Loschen_Zimmer(self.d, self.hotel)

    def anzeige(self):
        self.ghet = tk.Toplevel(self.root)
        self.print_zimmer = Print_Zimmer(self.ghet, self.hotel)


class Third:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Reservierungen Menu')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)  # Aici avem meniul pentru rezervari si functionalitatile sale

        self.button_one = tk.Button(self.top, text='Zuruck', command=self.close)
        self.button_one.pack(fill=tk.BOTH)

        self.button_two = tk.Button(self.top, text='Mach eine Reservierung', command=self.reservieren)
        self.button_two.pack(fill=tk.BOTH)

        self.button_three = tk.Button(self.top, text='Anzeige die Liste von Gästen, die aktuelle Reservierungen haben',
                                      command=self.aktuell)
        self.button_three.pack(fill=tk.BOTH)

        self.button_four = tk.Button(self.top, text='Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien ',
                                     command=self.filter)
        self.button_four.pack(fill=tk.BOTH)

        self.button_five = tk.Button(self.top, text='Anzeige alle Zimmer, die heute frei sind', command=self.free_today)
        self.button_five.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def reservieren(self):
        self.res = tk.Toplevel(self.root)
        self.reserv = Reservieren(self.res, self.hotel)

    def aktuell(self):
        self.a = tk.Toplevel(self.root)
        self.akt = Print_aktuell(self.a, self.hotel)

    def filter(self):
        self.f = tk.Toplevel(self.root)
        self.fil = Filter(self.f, self.hotel)

    def free_today(self):
        self.fr = tk.Toplevel(self.root)
        self.free = Anzeige_frei(self.fr, self.hotel)
