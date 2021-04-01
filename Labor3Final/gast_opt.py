from gaste import Gast
from test import valid_name


def add_guest(guest_list):
    # Fugt ein neuer Gast in die Liste falls seine Daten valid sind
    vorname = valid_name(str(input("Vorname:")))
    nachname = valid_name(str(input("Nachname:")))
    guest_list.append(Gast(vorname, nachname))
    print("Gast wurde erfolgreich eingefugt!")


def aktualisieren(guest_list):
    # Aktualisiert die Nachname eines Gastes die in die Liste von Gaste existiert
    vorname = valid_name(str(input("Vorname:")))
    nachname = valid_name(str(input("Aktueller Nachname:")))
    found = False
    for gast in guest_list:
        if gast.nachname == nachname and gast.vorname == vorname:
            gast.nachname = valid_name(str(input("Neuer Nachame:")))
            # Hier liest er die neue Nachname des Gastes
            print("Der Nachname wurde aktualisiert!")
            found = True
    if not found:
        print("Kein Gast mit diesem Nachname gefunden!")


def delete_gast(guest_list, res_list):
    # Loscht ein Gast aus der Liste falls er dort existiert
    vorname = valid_name(str(input("Vorname:")))
    nachname = valid_name(str(input("Nachname:")))
    out = False
    nr = 0
    while nr < len(guest_list):
        if guest_list[nr].vorname == vorname and guest_list[nr].nachname == nachname:
            # Die Liste von Gasten wurde durchquert und das gewunschte Gast wurde gefunden
            res1 = 0
            while res1 < len(guest_list[nr].lr):
                res2 = 0
                while res2 < len(res_list):
                    if guest_list[nr].lr[res1] == res_list[res2]:
                        res_list.pop(res2)
                        # Bevor wir das Gast loschen, loschen wir alle seine Reservierungen aus die Liste Res. per Hotel
                    else:
                        res2 += 1
                res1 += 1
            guest_list.pop(nr)
            # Erst hier wird das Gast aus der Liste Gaste geloscht
            print("Gast wurde erfolgreich entfernt!")
            out = True
            break
        else:
            nr += 1
    if not out:
        print("Kein Gast mit diesem Daten gefunden!")


def show_guest(guest_list):
    # Zeigt die Liste von Gaste falls sie mindestens ein Element hat
    if not guest_list:
        print("Die Liste ist leer!")
    else:
        for guest in guest_list:
            print(guest)
        # print(guest_list)
