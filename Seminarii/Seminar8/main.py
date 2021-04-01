from Rechenraum import Rechenraum
from Gebaude import Gebaude
from Raum import Raum


def main():
    ob1 = Rechenraum("Windows", "1a", 20)
    print(ob1)
    ob2 = Rechenraum("Linux", "2b", 30)
    print(ob2)
    ob3 = Raum("5c", 10)
    print(ob3)
    g = Gebaude([ob1, ob2, ob3], "G1")
    print(g.wievielplatz("1a"))


main()
