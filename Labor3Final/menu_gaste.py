from tools import delay
from gast_opt import *
from test import *


def menu():
    return "0.Zuruck \n1.Füge ein neuer Gast hin \n2.Aktualisierung der Nachname eines Gastes \n3.Löschung " \
           "eines Gastes \n4.Anzeige die Liste von Gästen"


def menu_gaste(guest_list, res_list):
    print(menu())
    x = int(input("Option:"))
    while x != 0:
        if x == 1:
            lange = len(guest_list)
            add_guest(guest_list)
            test_einfugen(guest_list, lange)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 2:
            aktualisieren(guest_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 3:
            delete_gast(guest_list, res_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        elif x == 4:
            show_guest(guest_list)
            delay()
            print(menu())
            x = int(input("Option:"))
        else:
            print("Error! Kein verfugbarer Menu!")
            print(menu())
            x = int(input("Option:"))
