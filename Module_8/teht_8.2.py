import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True,
         use_pure=True
         )

maakoodi = input("Anna maakoodi: ")

sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type"

print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()

for rivi in tulos:
    print("Lentokenttätyyppi:", rivi[0])
    print("Lukumäärä:", rivi[1])