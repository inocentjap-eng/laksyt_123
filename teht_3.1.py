#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen,
#ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
#samalla käyttäjälle, montako senttiä alimmasta sallitusta
#pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus = float(input("kuhan pituus: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen. Pituudesta puuttuu {puuttuu} cm.")

else:
    print("voi syoda kala")