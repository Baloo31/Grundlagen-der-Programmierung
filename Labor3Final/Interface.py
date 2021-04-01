from tkinter import *
from zimmern import Zimmer


class GUI:
    def __init__(self, gui_master, controller):
        self.__window = gui_master
        self.__controller = controller
        self.__roommenu = Frame(master=self.__window, borderwidth=5)
        self.__guestmenu = Frame(master=self.__window, borderwidth=5)
        self.__reservmenu = Frame(master=self.__window, borderwidth=5)
        self.__mainmenu = Frame(master=self.__window, borderwidth=5)
        self.populate_roommenu()
        self.populate_mainmenu()

    def add_room(self, nr, maxguest, price, color, sea_view):
        print(nr)
        print(int(maxguest))
        print(int(price))
        print(color)
        print(int(sea_view))
        room = Zimmer(int(nr), int(maxguest), int(price), color, int(sea_view))
        self.__controller.add_room(room)
