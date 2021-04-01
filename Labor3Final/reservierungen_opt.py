import datetime
from reservierungen import Reservierung
from test import valid_name


def reservieren(guest_list, res_list, room_list):
    print("Fur eine Reservierung braucht man ein Gast (Vorname und Nachname), Anzahl Personen "
          "und ein Zimmernummer!")
    res = 0  # Am Anfang behaupten wir dass keine Reservierung eingefugt wurde
    vorname = valid_name(input("Vorname:"))
    nachname = valid_name(input("Nachname:"))
    # Beide sollen valid sein
    num = int(input("Zimmernummer:"))
    anzp = int(input("Anzahl Personen:"))
    ci = datetime.date(int(input("Jahr:")), int(input("Monat:")), int(input("Anfangstag:")))
    co = datetime.date(int(input("Jahr:")), int(input("Monat:")), int(input("Endtag:")))
    today = datetime.date.today()  # Das heutige Datum wurde festgestellt
    for guest in guest_list:
        if guest.vorname == vorname and guest.nachname == nachname:
            # Hier fand man das Gast in die Liste von Gasten
            for room in room_list:
                # Hier sucht man fur das Zimmer und fragt man ob sie genug platz hat
                if room.num == num and room.anz >= anzp:
                    # Hier testet man ob das Zimmer leer ist
                    # Am Anfang behaupten wir dass sie leer ist
                    ver = 1
                    for el in res_list:
                        if el.zimmer == num:
                            if not (el.ci >= co or el.co <= ci):
                                ver = 0  # Falls wir hier angekommen sind, ist die Zimmer nicht leer
                                break
                    if ver == 1:
                        if (ci <= co) and (today <= ci):
                            guest.lr.append(Reservierung(num, anzp, ci, co))
                            res_list.append(Reservierung(num, anzp, ci, co))
                            print("Reservierung erfolgreich gemacht!")
                            res = 1
                        else:
                            print("Es wurde eine invalide Datum eingegeben!")
                    else:
                        print("Diese zimmer hat schon eine Reservierung in dieser Zeitspanne!")
    if res == 0:
        print("Die Reservierung konnte nicht gemacht werden! Bitte schauen Sie die eingefugten Daten nochmal an!")


def anzeige_lg(guest_list):
    # Zeigt die liste vin gaste die Reservierungen haben, falls Reservierungen gemacht wurden
    gef = 0
    for guest in guest_list:
        if guest.lr:
            print(guest)
            gef = 1
    if gef == 0:
        print("Es gibt keine Gaste mit aktuellen Reservierungen!")


def filtern(room_list):
    # Filtert alle Zimmern welche die Kriterien erfullen
    preis = int(input("Preis:"))
    meerblick = bool(input("Meerblick:"))
    gef = 0
    for room in room_list:
        if (room.preis <= preis) and (meerblick == room.meerblick):
            print(room)
            gef = 1
    if gef == 0:
        if meerblick:
            print("Es gibt keine Zimmern billiger als {} Euro mit Meerblick".format(preis))
        else:
            print("Es gibt keine Zimmern billiger als {} Euro ohne Meerblick".format(preis))


def heute_frei(res_list, room_list):
    # Zeigt welche Zimmern heute frei sind (Das heutige Datum)
    today = datetime.date.today()
    keine_frei = 1
    for room in room_list:
        leer = 1
        for res in res_list:
            if res.zimmer == room.num:
                if (res.ci <= today) and (res.co >= today):
                    leer = 0
                    break
        if leer == 1:
            print(room)
            keine_frei = 0
    if keine_frei == 1:
        print("Es gibt keine Zimmern die heute frei sind!")
