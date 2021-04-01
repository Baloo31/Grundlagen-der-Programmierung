from Repository.Repository import Rep
from tools import file
from menu_gaste import menu_gaste
from menu_zimmern import menu_zimmern
from menu_reservierungen import menu_res


def menu():
    return "0. Exit\n1. Menu Gaste \n2. Menu Zimmern \n3. Menu Reservierungen"


def main_menu():
    guest_list = []
    room_list = []
    datei = file()
    if datei:
        rep = Rep(datei)  # Hier bekommt man die Daten des ausgewahltes Datei
        rep.load_from_file(guest_list, room_list)
    res_list = []
    print(menu())
    x = int(input("Menu:"))
    while x != 0:
        if x == 1:
            menu_gaste(guest_list, res_list)
            print(menu())
            x = int(input("Menu:"))
        elif x == 2:
            menu_zimmern(room_list, guest_list, res_list)
            print(menu())
            x = int(input("Menu:"))
        elif x == 3:
            menu_res(guest_list, room_list, res_list)
            print(menu())
            x = int(input("Menu:"))
        else:
            print("Error! Kein verfugbarer Menu!")
            print(menu())
            x = int(input("Menu:"))


main_menu()
