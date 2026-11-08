import requests

API_AVAIN = "6b27493a6374c817bde84333a5f45c40"

kaupunki = input("Anna paikkakunnan nimi: ")

pyyntö = ("https://api.openweathermap.org/data/2.5/weather?q="
          + kaupunki + "&appid=" + API_AVAIN)

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()

        kuvaus = json_vastaus["weather"][0]["description"]
        kelvin = json_vastaus["main"]["temp"]
        celsius = kelvin - 273.15

        print("Säätila:", kuvaus)
        print(f"Lämpötila: {celsius:.1f} °C")
    elif vastaus.status_code == 404:
        print("Paikkakuntaa ei löytynyt.")
    elif vastaus.status_code == 401:
        print("Virheellinen API-avain.")
    else:
        print("Haku epäonnistui. Statuskoodi:", vastaus.status_code)
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")