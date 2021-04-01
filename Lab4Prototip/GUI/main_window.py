import tkinter as tk
from GUI.secondary_windows import First, Second, Third
from tkinter import messagebox


class Main:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Hotel Management')
        self.root.geometry('500x250')

        self.button_quit = tk.Button(self.root, text='Quit', command=self.close)
        self.button_quit.pack(fill=tk.BOTH)

        self.button_help = tk.Button(self.root, text='Help', command=self.help_msg)
        self.button_help.pack(fill=tk.BOTH)

        self.button_gast = tk.Button(self.root,  text='Menu Gaste', command=self.create_first_window)
        self.button_gast.pack(fill=tk.BOTH)

        self.button_zim = tk.Button(self.root, text='Menu Zimmern', command=self.create_second_window)
        self.button_zim.pack(fill=tk.BOTH)

        self.button_res = tk.Button(self.root, text='Menu Gemeinsam', command=self.create_third_window)
        self.button_res.pack(fill=tk.BOTH)

    def create_first_window(self):
        self.first_window = tk.Toplevel(self.root)
        self.first = First(self.first_window, self.hotel)

    def create_second_window(self):
        self.second_window = tk.Toplevel(self.root)
        self.second = Second(self.second_window, self.hotel)

    def create_third_window(self):
        self.third_window = tk.Toplevel(self.root)
        self.third = Third(self.third_window, self.hotel)

    def close(self):
        self.root.destroy()

    def help_msg(self):
        message = "1. Menu Gaste" \
                  "\n2. Menu Zimmern" \
                  "\n3. Menu Gemeinsam" \
                  "\n\n\n" \
                  "1. Menu Gaste: " \
                  "\n\na. Zuruck" \
                  "\nb. Füge ein neuer Gast hin" \
                  "\nc. Aktualisierung der Nachname eines Gastes" \
                  "\nd. Löschung eines Gastes" \
                  "\ne. Anzeige die Liste von Gästen" \
                  "\n\n\n" \
                  "2. Menu Zimmern: " \
                  "\n\na. Zuruck" \
                  "\nb. Füge ein Zimmer hin" \
                  "\nc. Aktualisierung des Preises eines Zimmers" \
                  "\nd. Löschung eines Zimmers" \
                  "\ne. Anzeige die Liste von Zimmern" \
                  "\n\n\n" \
                  "3. Menu Gemeinsam:" \
                  "\n\na. Zuruck" \
                  "\nb. Mach eine Reservierung" \
                  "\nc. Anzeige die Liste von Gästen, die aktuelle Reservierungen haben" \
                  "\nd. Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien (z. B. ein Zimmer billiger" \
                  "als 100 Euro, mit Meerblick)" \
                  "\ne. Anzeige alle Zimmer, die heute frei sind"
        messagebox.showinfo(title="Help menu", message=message)
