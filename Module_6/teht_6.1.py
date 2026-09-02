import random

def heitä_noppaa():
    luku = random.randint(1,6)
    return luku

heitto = 0

while heitto != 6:
    heitto = heitä_noppaa()
    print(f"heitit on: {heitto}")