from tkinter import Tk
from GUI.main_window import Main
from Entities.Hotel import Hotel
from Repository.Repository import Rep
from tkinter.filedialog import askopenfilename


def main():
    hotel = Hotel()
    files = []
    #  Obtinem calea primului fisier (Oaspeti)
    x = Tk()
    x.withdraw()  # Ascundem fereastra goala de pe fundal si lasam doar casuta de alegere a unui fisier
    file = askopenfilename(title="Bitte wahlen sie eine Datei fur Gaste!", filetype=(("Text files", ".txt"),
                                                                                     ("All files", ".*")))

    x.destroy()
    if file != '':
        files.append(file)
    #  Obtinem calea celui de al doilea fisier (Camere)
    x = Tk()
    x.withdraw()
    file = askopenfilename(title="Bitte wahlen sie eine Datei fur Zimmern !", filetype=(("Text files", ".txt"),
                                                                                        ("All files", ".*")))
    x.destroy()
    if file != '':
        files.append(file)
    #  Obtinem calea celui de al treilea fisier (Rezervari)
    x = Tk()
    x.withdraw()
    file = askopenfilename(title="Bitte wahlen sie eine Datei fur Reservierungen!", filetype=(("Text files", ".txt"),
                                                                                              ("All files", ".*")))
    x.destroy()
    if file != '':
        files.append(file)

    # files = [r"C:\Users\Asus\Desktop\Hotel\gaste.txt", r"C:\Users\Asus\Desktop\Hotel\zimmern.txt",
    # r"C:\Users\Asus\Desktop\Hotel\reservierungen.txt"]
    # In varianta comentata, calea fisierelor a fost specificata in cadrul programului

    if len(files) == 3:
        # Lansarea aplicatiei cu salvare si incarcare din fisier
        rep = Rep(files[0], files[1], files[2])
        rep.load_from_file(hotel)

        root = Tk()
        Main(root, hotel)
        root.mainloop()

        rep.store_to_file(hotel)
    else:
        # In cazul in care nu a fost alese toate fisierele sursa/destinatie se
        # va rula ca si cum nu a fost selectat vreunul
        root = Tk()
        Main(root, hotel)
        root.mainloop()


main()
