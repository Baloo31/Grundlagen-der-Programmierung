from gaste import Gast
from zimmern import Zimmer


class Rep:
    def __init__(self, file):
        self.__f_name = file

    def load_from_file(self, guest_list, room_list):
        file = open(self.__f_name, "r")
        # Offnen des Dateis
        limit_line = False
        # limit_line bestimmt ob die Linie zwischen Gaste und Zimmern angetroffen wurde
        # So weiss man ob Gaste oder Zimmern einfugt werden sollen
        for line in file:
            if line.strip() != "-":
                if not limit_line:
                    # Einfugen einer Gast
                    data = line.strip().split(";")
                    guest_list.append(Gast(data[0], data[1]))
                else:
                    # Einfugen einer Zimmer
                    data = line.strip().split(";")
                    room_list.append(Zimmer(int(data[0]), int(data[1]), int(data[2]), data[3], bool(data[4])))
            else:
                # Linie zwischen Gaste und Zimmern wurde gefunden
                limit_line = True
        file.close()
