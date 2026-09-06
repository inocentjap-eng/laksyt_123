lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto: uusi, haku tai lopeta: ").lower()

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} tallennettiin koodilla {icao}.")

    elif toiminto == "haku":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()

        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaava lentoasema on {lentoasemat[icao]}.")
        else:
            print(f"ICAO-koodilla {icao} ei löytynyt lentoasemaa.")

    elif toiminto == "lopeta":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen toiminto. Valitse uusi, haku tai lopeta.")