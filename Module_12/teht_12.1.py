import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
    else:
        print("Vitsin haku epäonnistui. Statuskoodi:", vastaus.status_code)
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")