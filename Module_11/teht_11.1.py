class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print("Kirja: " + self.nimi)
        print("Kirjoittaja: " + self.kirjoittaja)
        print("Sivumäärä: " + str(self.sivumäärä))


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print("Lehti: " + self.nimi)
        print("Päätoimittaja: " + self.päätoimittaja)


# Pääohjelma

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_6.tulosta_tiedot()