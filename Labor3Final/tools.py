from tkinter.filedialog import askopenfilename  # Fur das Suchen einer Datei im Computer
from tkinter import *


def file():
    Tk().withdraw()
    return askopenfilename(title="Bitte wahlen sie eine Datei !", filetype=(("Text files", ".txt"),
                                                                            ("All files", ".*")))


def delay():
    input("Drucken sie bitte auf die 'Enter' taste..")
