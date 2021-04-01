# from Rational import Rational
from auto import Auto
from kunde import Kunde
from autohaus import Autohaus


def main():
    """
    x = Rational(1, 2)
    y = Rational(3, 5)
    print(x.add(y))
    print(x.sub(y))
    print(x.mul(y))
    print(x.div(y))
    """
    logan = Auto("Logan", "Schwarz", "2007")
    passat = Auto("Passat", "Grau", "2005")
    bmw = Auto("Bmw", "Grau", "2001")
    ion = Kunde("Ion", 2000)
    ah = Autohaus()
    ah.add_auto(logan)
    ah.add_auto(passat)
    ah.add_auto(bmw)
    ah.sell_auto(bmw, ion)
    print(ah.autos, ah.solds)


main()
