from tools import delay
from zimmer_opt import *
from test import *


def menu():
    return "0.Zuruck\n1.Füge ein Zimmer hin\n2.Aktualisierung des " \
           "Preises eines Zimmers\n3.Löschung eines Zimmers\n4.Anzeige die Liste von Zimmern"


def menu_zimmern(room_list, guest_list, res_list):
    print(menu())
    x = int(input("Option:"))
    while x != 0:
        if x == 1:
            lange = len(room_list)
            add_room(room_list)
            test_einfugen(room_list, lange)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 2:
            aktualisieren_p(room_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 3:
            delete_room(room_list, guest_list, res_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 4:
            show_room(room_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        else:
            print("Error! Kein verfugbarer Menu!")
            print(menu())
            x = int(input("Option:"))
