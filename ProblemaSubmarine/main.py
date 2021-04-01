from PreluareDateFisier.preluare import Pre
from random import random, seed, randint


def distribuire_marinari(submarin, lista_marinari):
    if 2 * submarin.lista_cabine > (lista_marinari[0]+lista_marinari[1]) or lista_marinari[1] < 2:
        return "Atentie, nu s-au distribuit suficienti marinari pentru submarinul {}!".format(submarin)
    else:
        submarin.nr_marinari = 2 * submarin.lista_cabine
        ma = lista_marinari[0]
        mm = lista_marinari[1]
        lista_marinari[0] -= 2 * submarin.lista_cabine - 2
        lista_marinari[1] -= 2
        return "S-au putut distribui {} marinari, din care 2 masinisti ! Au ramas nedistribuiti {} " \
               "marinari".format(2 * submarin.lista_cabine, (ma+mm)-2*submarin.lista_cabine)


def deplasare(submarin, x, y, raza):
    x_prim = int((x + submarin.x) / 2 - raza)
    y_prim = int((y + submarin.y) / 2 - raza)
    return "Submarinul {} se va deplasa la punctul de coordonate x: {} si y: {}".format(submarin, x_prim, y_prim)


def main():

    lista_submarine = []

    pre = Pre("submarine", lista_submarine)
    pre.load_from_file()
    print(lista_submarine)

    cheie_criptare = input("Cheie_criptare:")
    while not cheie_criptare.isnumeric():
        print("Cheia de criptare trebuie sa fie numerica !")
        cheie_criptare = input("Cheie_criptare:")
    print(lista_submarine[0].raporteaza_situatie(int(cheie_criptare)))

    lista_marinari = [10, 4]  # Marinari, respectiv marinari masinisti
    for submarin in lista_submarine:
        print(distribuire_marinari(submarin, lista_marinari))

    for submarin in lista_submarine:
        print(deplasare(submarin, 0, 0, 3))


main()
