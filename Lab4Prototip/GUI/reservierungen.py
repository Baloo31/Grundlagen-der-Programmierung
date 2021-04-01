import tkinter as tk
import datetime
from Entities.Reserv import Reservierung
from tkinter import messagebox


class Reservieren:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Mach eine Reservierung')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.vorname = tk.Entry(self.root)
        self.vorname.insert(0, "Vorname")
        self.vorname.config(state=tk.DISABLED)
        self.vorname.bind("<Button-1>", self.click_vorname)
        self.vorname.pack()

        self.nachname = tk.Entry(self.root)
        self.nachname.insert(0, "Nachname")
        self.nachname.config(state=tk.DISABLED)
        self.nachname.bind("<Button-1>", self.click_nachname)
        self.nachname.pack()

        self.num = tk.Entry(self.root)
        self.num.insert(0, "Zimmernumer")
        self.num.config(state=tk.DISABLED)
        self.num.bind("<Button-1>", self.click_num)
        self.num.pack()

        self.anz = tk.Entry(self.root)
        self.anz.insert(0, "Anzahl Personen")
        self.anz.config(state=tk.DISABLED)
        self.anz.bind("<Button-1>", self.click_anz)
        self.anz.pack()

        self.ci_jahr = tk.Entry(self.root)
        self.ci_jahr.insert(0, "Check In Jahr")
        self.ci_jahr.config(state=tk.DISABLED)
        self.ci_jahr.bind("<Button-1>", self.click_ci_jahr)
        self.ci_jahr.pack()

        self.ci_monat = tk.Entry(self.root)
        self.ci_monat.insert(0, "Check In Monat")
        self.ci_monat.config(state=tk.DISABLED)
        self.ci_monat.bind("<Button-1>", self.click_ci_monat)
        self.ci_monat.pack()

        self.ci_tag = tk.Entry(self.root)
        self.ci_tag.insert(0, "Check In Tag")
        self.ci_tag.config(state=tk.DISABLED)
        self.ci_tag.bind("<Button-1>", self.click_ci_tag)
        self.ci_tag.pack()

        self.co_jahr = tk.Entry(self.root)
        self.co_jahr.insert(0, "Check Out Jahr")
        self.co_jahr.config(state=tk.DISABLED)
        self.co_jahr.bind("<Button-1>", self.click_co_jahr)
        self.co_jahr.pack()

        self.co_monat = tk.Entry(self.root)
        self.co_monat.insert(0, "Check Out Monat")
        self.co_monat.config(state=tk.DISABLED)
        self.co_monat.bind("<Button-1>", self.click_co_monat)
        self.co_monat.pack()

        self.co_tag = tk.Entry(self.root)
        self.co_tag.insert(0, "Check Out Tag")
        self.co_tag.config(state=tk.DISABLED)
        self.co_tag.bind("<Button-1>", self.click_co_tag)
        self.co_tag.pack()

        self.button = tk.Button(self.top, text='Reserviere', command=self.reserviere)
        self.button.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Back', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def click_vorname(self, event):
        self.vorname.config(state=tk.NORMAL)
        self.vorname.delete(0, tk.END)

    def click_nachname(self, event):
        self.nachname.config(state=tk.NORMAL)
        self.nachname.delete(0, tk.END)

    def click_num(self, event):
        self.num.config(state=tk.NORMAL)
        self.num.delete(0, tk.END)

    def click_anz(self, event):
        self.anz.config(state=tk.NORMAL)
        self.anz.delete(0, tk.END)

    def click_ci_jahr(self, event):
        self.ci_jahr.config(state=tk.NORMAL)
        self.ci_jahr.delete(0, tk.END)

    def click_ci_monat(self, event):
        self.ci_monat.config(state=tk.NORMAL)
        self.ci_monat.delete(0, tk.END)

    def click_ci_tag(self, event):
        self.ci_tag.config(state=tk.NORMAL)
        self.ci_tag.delete(0, tk.END)

    def click_co_jahr(self, event):
        self.co_jahr.config(state=tk.NORMAL)
        self.co_jahr.delete(0, tk.END)

    def click_co_monat(self, event):
        self.co_monat.config(state=tk.NORMAL)
        self.co_monat.delete(0, tk.END)

    def click_co_tag(self, event):
        self.co_tag.config(state=tk.NORMAL)
        self.co_tag.delete(0, tk.END)

    def reserviere(self):
        today = datetime.date.today()
        vorname = self.vorname.get()
        nachname = self.nachname.get()
        num = int(self.num.get())
        anz = int(self.anz.get())
        ci = datetime.date(int(self.ci_jahr.get()), int(self.ci_monat.get()), int(self.ci_tag.get()))
        co = datetime.date(int(self.co_jahr.get()), int(self.co_monat.get()), int(self.co_tag.get()))
        res = 0
        for guest in self.hotel.gaste:
            if guest.vorname == vorname and guest.nachname == nachname:  # Cauta oaspetele in lista
                for room in self.hotel.zimmern:
                    if room.num == num and room.anz >= anz:  # Cauta camera si verifica daca are suficiente locuri
                        ver = 1
                        for el in self.hotel.reservierungen:
                            if el.zimmer == num:
                                if not (el.ci > co or el.co < ci):
                                    ver = 0  # In cazul in care conditia ne-a adus aici camera cautata nu este libera
                                    break
                        if ver == 1:
                            if (ci <= co) and (today <= ci):
                                guest.lr.append(Reservierung(num, anz, ci, co))
                                self.hotel.reservierungen.append(Reservierung(num, anz, ci, co))
                                tk.messagebox.showinfo(title="Erfolg", message="Reservierung erfolgreich gemacht!")
                                res = 1
        if res == 0:
            tk.messagebox.showerror(title="Error", message="Reservierung konnte nicht gemacht werden, "
                                                           "weil eine Reservierung in dieser Zeitspanne schon gibt, "
                                                           "oder Gast, Zimmer und Datum sind invalid!")


class Print_aktuell:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Gaste die aktuelle Reservierungen haben')
        self.root.geometry('700x500')

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)
        nr = 1
        for el in self.hotel.gaste:
            if el.lr:
                self.text.insert(tk.END, "Gast {}. : ".format(nr) + el.vorname + " " + el.nachname + '\n')
                nr += 1
        if nr == 1:
            self.text.insert(tk.END, "Keine Gaste mit aktuelle Reservierungen !")
        self.text.pack()

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gemeinsam', command=self.close)
        self.back.pack()

        self.top.pack()

    def close(self):
        self.root.destroy()


class Filter:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Kriterien')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)

        self.preis = tk.Entry(self.root)
        self.preis.insert(0, "Preis")
        self.preis.config(state=tk.DISABLED)
        self.preis.bind("<Button-1>", self.click_preis)
        self.preis.pack()

        self.mb = tk.Entry(self.root)
        self.mb.insert(0, "Meerblick")
        self.mb.config(state=tk.DISABLED)
        self.mb.bind("<Button-1>", self.click_mb)
        self.mb.pack()

        self.filter = tk.Button(self.top, text='Filter', command=self.filter_print)
        self.filter.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gemeinsam', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.top.pack()

    def close(self):
        self.root.destroy()

    def click_preis(self, event):
        self.preis.config(state=tk.NORMAL)
        self.preis.delete(0, tk.END)

    def click_mb(self, event):
        self.mb.config(state=tk.NORMAL)
        self.mb.delete(0, tk.END)

    def filter_print(self):
        self.f = tk.Toplevel(self.root)
        self.fil = Anzeige(self.f, self.hotel, int(self.preis.get()), self.mb.get())


class Anzeige:
    def __init__(self, root, hotel, preis, mb):
        self.root = root
        self.hotel = hotel
        self.preis = preis
        if mb == "Ja":
            self.mb = True
        else:
            self.mb = False
        self.root.title('Anzeige Gefiltert')
        self.root.geometry('500x250')

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)
        nr = 1
        for el in self.hotel.zimmern:
            if el.preis <= self.preis and self.mb == el.meerblick:
                self.text.insert(tk.END, "Zimmer {} ".format(el.num) + '\n')
                nr += 1
        if nr == 1:
            if self.mb:
                self.text.insert(tk.END, "Es gibt keine Zimmern billiger als {} Euro mit Meerblick".format(self.preis))
            else:
                self.text.insert(tk.END, "Es gibt keine Zimmern billiger als {} Euro ohne Meerblick".format(self.preis))
        self.text.pack()

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gemeinsam', command=self.close)
        self.back.pack()

        self.top.pack()

    def close(self):
        self.root.destroy()


class Anzeige_frei:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Zimmern die heute frei sind')
        self.root.geometry('700x500')
        self.today = datetime.date.today()

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)
        keine_frei = 1
        for room in self.hotel.zimmern:
            leer = 1
            for res in self.hotel.reservierungen:
                if res.zimmer == room.num:
                    if (res.ci <= self.today) and (res.co >= self.today):
                        leer = 0
                        break
            if leer == 1:
                self.text.insert(tk.END, "Zimmer {} ".format(room.num) + '\n')
                keine_frei = 0
        if keine_frei == 1:
            self.text.insert(tk.END, "Es gibt keine Zimmern die heute frei sind!")

        self.text.pack()

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gemeinsam', command=self.close)
        self.back.pack()

        self.top.pack()

    def close(self):
        self.root.destroy()
