import random
def heittä_nopaa(tahkot):
    luku = random.randint(1,tahkot)
    return luku

max_silmäluku = int(input("Kuinka monta tahkoa nopassa on? "))

heitto = 0

while heitto != max_silmäluku:
    heitto = heittä_nopaa(max_silmäluku)
    print(f"heittit on: {heitto}")