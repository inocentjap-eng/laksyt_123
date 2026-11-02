class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print("Hissi on nyt kerroksessa " + str(self.kerros))

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print("Hissi on nyt kerroksessa " + str(self.kerros))

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print("Kerrosta " + str(kohde) + " ei ole olemassa")
            return
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lukumäärä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Hissiä " + str(hissin_numero) + " ei ole olemassa")
            return
        print("Ajetaan hissiä " + str(hissin_numero))
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)


# Pääohjelma

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 4)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(1, 1)