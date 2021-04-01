import tkinter as tk
from Entities.Zimmer import Zimmer
from tkinter import messagebox


class Add_Room:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Einfugen Zimmer')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.numer = tk.Entry(self.root)
        self.numer.insert(0, "Zimmernumer")
        self.numer.config(state=tk.DISABLED)
        self.numer.bind("<Button-1>", self.click_numer)
        self.numer.pack()

        self.anzahl = tk.Entry(self.root)
        self.anzahl.insert(0, "Anzahl Personen")
        self.anzahl.config(state=tk.DISABLED)
        self.anzahl.bind("<Button-1>", self.click_anzahl)
        self.anzahl.pack()

        self.preis = tk.Entry(self.root)
        self.preis.insert(0, "Preis / Nacht")
        self.preis.config(state=tk.DISABLED)
        self.preis.bind("<Button-1>", self.click_preis)
        self.preis.pack()

        self.farbe = tk.Entry(self.root)
        self.farbe.insert(0, "Farbe")
        self.farbe.config(state=tk.DISABLED)
        self.farbe.bind("<Button-1>", self.click_farbe)
        self.farbe.pack()

        self.mb = tk.Entry(self.root)
        self.mb.insert(0, "Meerblick")
        self.mb.config(state=tk.DISABLED)
        self.mb.bind("<Button-1>", self.click_mb)
        self.mb.pack()

        self.button = tk.Button(self.top, text='Add', command=self.add_zimmer)
        self.button.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Back', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def add_zimmer(self):
        self.hotel.zimmern.append(Zimmer(int(self.numer.get()), int(self.anzahl.get()), int(self.preis.get()),
                                         str(self.farbe.get()), bool(self.mb.get())))
        messagebox.showinfo(title="Erfolg", message="Zimmer wurde erfolgreich eingefugt!")

    def close(self):
        self.root.destroy()

    def click_numer(self, event):
        self.numer.config(state=tk.NORMAL)
        self.numer.delete(0, tk.END)

    def click_anzahl(self, event):
        self.anzahl.config(state=tk.NORMAL)
        self.anzahl.delete(0, tk.END)

    def click_preis(self, event):
        self.preis.config(state=tk.NORMAL)
        self.preis.delete(0, tk.END)

    def click_farbe(self, event):
        self.farbe.config(state=tk.NORMAL)
        self.farbe.delete(0, tk.END)

    def click_mb(self, event):
        self.mb.config(state=tk.NORMAL)
        self.mb.delete(0, tk.END)


class Aktualisiere_Preis:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Aktualisiere Preis')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.numer = tk.Entry(self.root)
        self.numer.insert(0, "Zimmernumer")
        self.numer.config(state=tk.DISABLED)
        self.numer.bind("<Button-1>", self.click_numer)
        self.numer.pack()

        self.neu_preis = tk.Entry(self.root)
        self.neu_preis.insert(0, "Neuer Preis / Nacht")
        self.neu_preis.config(state=tk.DISABLED)
        self.neu_preis.bind("<Button-1>", self.click_neu_preis)
        self.neu_preis.pack()

        self.update = tk.Button(self.top, text="Aktualisiere", command=self.update_preis)
        self.update.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Back', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def click_numer(self, event):
        self.numer.config(state=tk.NORMAL)
        self.numer.delete(0, tk.END)

    def click_neu_preis(self, event):
        self.neu_preis.config(state=tk.NORMAL)
        self.neu_preis.delete(0, tk.END)

    def update_preis(self):
        akt = False
        for el in self.hotel.zimmern:
            if el.num == int(self.numer.get()):
                el.preis = self.neu_preis.get()
                messagebox.showinfo(title="Erfolg!", message="Preis wurde erfolgreich aktualisiert!")
                akt = True
        if not akt:
            messagebox.showerror(title="Error", message="Zimmer konnte nicht gefunden werden!")


class Print_Zimmer:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Die Liste von Zimmern')
        self.root.geometry('700x500')

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)
        nr = 1
        for el in self.hotel.zimmern:
            self.text.insert(tk.END, "Zimmer : " + str(el) + '\n')
            nr += 1
        if nr == 1:
            self.text.insert(tk.END, "Die Liste von Zimmern ist Leer !")
        self.text.pack()

        self.back = tk.Button(self.top, text='Zuruck zum Menu Zimmern', command=self.close)
        self.back.pack()

        self.top.pack()

    def close(self):
        self.root.destroy()


class Loschen_Zimmer:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Loschen Zimmer')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.numer = tk.Entry(self.root)
        self.numer.insert(0, "Zimmernumer")
        self.numer.config(state=tk.DISABLED)
        self.numer.bind("<Button-1>", self.click_numer)
        self.numer.pack()

        self.loschen = tk.Button(self.top, text='Loschen', command=self.delete)
        self.loschen.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Zuruck zum Menu Zimmern', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def click_numer(self, event):
        self.numer.config(state=tk.NORMAL)
        self.numer.delete(0, tk.END)

    def close(self):
        self.root.destroy()

    def delete(self):
        numer = int(self.numer.get())  # Obtinem valoarea din Entry
        nr = 0
        out = False
        while nr < len(self.hotel.zimmern):
            if self.hotel.zimmern[nr].num == numer:
                res = 0
                while res < len(self.hotel.reservierungen):  # Scoate rezervarile
                    if self.hotel.zimmern[nr].num == self.hotel.reservierungen[res].zimmer:
                        self.hotel.reservierungen.pop(res)
                    else:
                        res += 1
                for guest in self.hotel.gaste:  # Scoate rezervarile din toate listele de rezervari ale oaspetilor
                    res1 = 0
                    while res1 < len(guest.lr):
                        if guest.lr[res1].zimmer == numer:
                            guest.lr.pop(res1)
                        else:
                            res1 += 1
                self.hotel.zimmern.pop(nr)  # Scoate din lista de camere
                messagebox.showinfo(title="Erfolg!", message="Zimmer wurde erfolgreich entfernt!")
                out = True
                break
            else:
                nr += 1
        if not out:
            messagebox.showerror(title="Error", message="Kein Zimmer mit diesem Daten gefunden!")
