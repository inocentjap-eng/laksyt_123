import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True,
         use_pure=True
         )

koodi1 = input("Anna lentoaseman ICAO-koodi: ")
koodi2 = input("Anna lentoaseman ICAO-koodi: ")

sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{koodi1}'"

print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos1 = kursori.fetchall()

sq = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{koodi2}'"

print(sq)
kursori = yhteys.cursor()
kursori.execute(sq)
tulos2 = kursori.fetchall()

if len(tulos1) > 0 and len(tulos2) > 0:
    koordinaatit1 = tulos1[0]
    koordinaatit2 = tulos2[0]

    etäisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etäisyys:.1f} km")
else:
    print("Jompaakumpaa lentokenttää ei löytynyt.")

