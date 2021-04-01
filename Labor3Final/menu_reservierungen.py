from tools import delay
from reservierungen_opt import *
from test import *


def menu():
    return "0.Zuruck\n1.Mach eine Reservierung\n2.Anzeige die Liste von Gästen, die aktuelle Reservierungen " \
           "haben\n3.Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien (z. B. ein Zimmer billiger " \
           "als 100 Euro, mit Meerblick)\n4.Anzeige alle Zimmer, die heute frei sind"


def menu_res(guest_list, room_list, res_list):
    print(menu())
    x = int(input("Option:"))
    while x != 0:
        if x == 1:
            lange = len(res_list)
            reservieren(guest_list, res_list, room_list)
            test_einfugen(res_list, lange)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 2:
            anzeige_lg(guest_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 3:
            filtern(room_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 4:
            heute_frei(res_list, room_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        else:
            print("Error! Kein verfugbarer Menu!")
            print(menu())
            x = int(input("Option:"))
