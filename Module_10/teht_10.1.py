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


# Pääohjelma

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)