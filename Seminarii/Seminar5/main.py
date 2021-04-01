from auto import Auto
from autos import AutoBox


def main():
    autos = AutoBox()

    a1 = Auto("blau", "Normal", 8, "dacia")
    a2 = Auto("rot", "Sport", 12, "lada")
    a3 = Auto("grau", "Eco", 8, "dacia")
    a4 = Auto("pink", "Normal", 8, "oltcit")

    autos.add_auto(a1)
    autos.add_auto(a2)
    autos.add_auto(a3)
    autos.add_auto(a4)
    autos.remove_cars()
    for auto in autos.get_autos():
        print(auto)

    print(autos.sum_ver())
    print(autos.durchschnittsverbrauch())


main()
