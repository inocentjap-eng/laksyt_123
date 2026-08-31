import random

oikea_luku = random.randint(1, 10)
arvaus = 0

while arvaus != oikea_luku:
    arvaus = int(input("Arvaa luku väliltä 1–10: "))

    if arvaus > oikea_luku:
        print("Liian suuri arvaus")
    elif arvaus < oikea_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")