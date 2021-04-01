import tkinter as tk
from Entities.Gast import Gast
from tkinter import messagebox


class Add_Guest:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Einfugen Gast')
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

        self.button = tk.Button(self.top, text='Add', command=self.add_guest)
        self.button.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Back', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def add_guest(self):
        vorname = self.vorname.get()
        nachname = self.nachname.get()
        if valid_name(vorname) and valid_name(nachname):
            self.hotel.gaste.append(Gast(vorname, nachname, []))
            messagebox.showinfo(title="Erfolg!", message="Gast wurde erfolgreich eingefugt!")
        else:
            messagebox.showerror(title="Error", message="Invalider Name")


    def close(self):
        self.root.destroy()

    def click_vorname(self, event):
        self.vorname.config(state=tk.NORMAL)
        self.vorname.delete(0, tk.END)

    def click_nachname(self, event):
        self.nachname.config(state=tk.NORMAL)
        self.nachname.delete(0, tk.END)


class Update_Guest:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Aktualisiere Nachname')
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

        self.neu_name = tk.Entry(self.root)
        self.neu_name.insert(0, "Neuer Nachname")
        self.neu_name.config(state=tk.DISABLED)
        self.neu_name.bind("<Button-1>", self.click_neu_name)
        self.neu_name.pack()

        self.update = tk.Button(self.top, text="Aktualisiere", command=self.update_nachname)
        self.update.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Back', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def close(self):
        self.root.destroy()

    def update_nachname(self):
        vorname = self.vorname.get()
        nachname = self.nachname.get()
        neu_name = self.neu_name.get()
        akt = 0
        if valid_name(vorname) and valid_name(nachname) and valid_name(neu_name):
            for el in self.hotel.gaste:
                if el.vorname == vorname and el.nachname == nachname:
                    el.nachname = neu_name
                    messagebox.showinfo(title="Erfolg", message="Erfolgreich aktualisiet !")
                    akt = 1
            if akt == 0:
                messagebox.showerror(title="Error", message="Kein Gast mit diesen Daten gefunden")
        else:
            messagebox.showerror(title="Error", message="Invalider Name")


    def click_vorname(self, event):
        self.vorname.config(state=tk.NORMAL)
        self.vorname.delete(0, tk.END)

    def click_nachname(self, event):
        self.nachname.config(state=tk.NORMAL)
        self.nachname.delete(0, tk.END)

    def click_neu_name(self, event):
        self.neu_name.config(state=tk.NORMAL)
        self.neu_name.delete(0, tk.END)


class Print_Gast:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Die Liste von Gaste')
        self.root.geometry('700x500')

        self.top = tk.Frame(self.root)

        self.text = tk.Text(self.root)
        nr = 1
        for el in self.hotel.gaste:
            self.text.insert(tk.END, "Gast {}. : ".format(nr) + str(el) + '\n')
            nr += 1
        if nr == 1:
            self.text.insert(tk.END, "Die Liste von Gaste ist Leer !")
        self.text.pack()

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gaste', command=self.close)
        self.back.pack()

        self.top.pack()

    def close(self):
        self.root.destroy()


class Delete_Guest:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.root.title('Loschen Gast')
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

        self.loschen = tk.Button(self.top, text='Loschen', command=self.delete)
        self.loschen.pack(fill=tk.BOTH)

        self.back = tk.Button(self.top, text='Zuruck zum Menu Gaste', command=self.close)
        self.back.pack(fill=tk.BOTH)

        self.text = tk.Text(self.top)
        self.text.pack(fill=tk.BOTH)
        self.top.pack()

    def click_vorname(self, event):
        self.vorname.config(state=tk.NORMAL)
        self.vorname.delete(0, tk.END)

    def click_nachname(self, event):
        self.nachname.config(state=tk.NORMAL)
        self.nachname.delete(0, tk.END)

    def close(self):
        self.root.destroy()

    def delete(self):
        vorname = self.vorname.get()
        nachname = self.nachname.get()
        out = False
        nr = 0
        while nr < len(self.hotel.gaste):
            if self.hotel.gaste[nr].vorname == vorname and self.hotel.gaste[nr].nachname == nachname:
                res1 = 0
                while res1 < len(self.hotel.gaste[nr].lr):
                    res2 = 0
                    while res2 < len(self.hotel.reservierungen):
                        if self.hotel.gaste[nr].lr[res1] == self.hotel.reservierungen[res2]:
                            self.hotel.reservierungen.pop(res2)
                        else:
                            res2 += 1
                    res1 += 1
                self.hotel.gaste.pop(nr)
                messagebox.showinfo(title="Erfolg!", message="Gast wurde erfolgreich entfernt!")
                out = True
                break
            else:
                nr += 1
        if not out:
            messagebox.showerror(title="Error", message="Kein Gast mit diesem Daten gefunden!")


def valid_name(name):
    if name != "":
        nr = 0
        while nr < len(name) and name[nr] in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            nr += 1
        if nr < len(name):
            return False
        else:
            return True
    else:
        return False
