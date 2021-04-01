from zimmern import Zimmer
from test import valid_name


def show_room(room_list):
    # Zeigt die liste der Zimmern, falls es mindestens ein Zimmer gibt
    if not room_list:
        print("Die Liste ist leer!")
    else:
        for room in room_list:
            print(room)
        # print(room_list)


def delete_room(room_list, guest_list, res_list):
    # Entfernt ein Zimmer mit ein gegebenen Zimmernummer aus der Liste falls sie dort existiert
    nummer = int(input("Zimmernummer:"))
    nr = 0
    out = False
    # Am Anfang sucht man die Zimmer
    while nr < len(room_list):
        if room_list[nr].num == nummer:
            res = 0
            # Man loscht alle Res. fur dieses Zimmer aus der Liste Res. per Hotel
            while res < len(res_list):
                if room_list[nr].num == res_list[res].zimmer:
                    res_list.pop(res)
                else:
                    res += 1
            # Man loscht alle Res. fur dieses Zimmer aus der Liste Res. jeder Gast
            for guest in guest_list:
                res1 = 0
                while res1 < len(guest.lr):
                    if guest.lr[res1].zimmer == nummer:
                        guest.lr.pop(res1)
                    else:
                        res1 += 1
            # Erst hier wird das Zimmer aus der Zimmerliste geloscht
            room_list.pop(nr)
            print("Zimmer wurde erfolgreich entfernt!")
            out = True
            break
        else:
            nr += 1
    if not out:
        print("Kein Zimmer mit diesem Daten gefunden!")


def aktualisieren_p(room_list):
    # Aktualisiert die Preis eines Zimmers falls sie in die Liste existiert
    nr = int(input("Zimmernummer:"))
    found = False
    for zimmer in room_list:
        if zimmer.num == nr:
            zimmer.preis = int(input("Neuer Preis:"))
            print("Preis wurde erfolgreich aktualisiert!")
            found = True
    if not found:
        print("Kein Zimmer mit diesem Nummer gefunden")


def add_room(room_list):
    # Fugt ein neues Zimmer in die liste von Zimmern
    room_list.append(Zimmer(int(input("Zimmernummer:")), int(input("Anzahl moglichen Gasten:")),
                             int(input("Preis:")), valid_name(str(input("Farbe:"))), bool(input("Meerblick:"))))
    # Das Attribut Farbe wurde mit valid_name getestet
    print("Zimmer wurde erfolgreich eingefugt!")
