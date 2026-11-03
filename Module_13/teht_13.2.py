from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="flight_game",
    use_pure=True
)

def hae_kentta(icao):
    kursori = yhteys.cursor()
    kursori.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (icao,))
    return kursori.fetchone()

@app.route('/kenttä/<icao>')
def kentta(icao):
    try:
        rivi = hae_kentta(icao.upper())
        if rivi is None:
            tilakoodi = 404
            vastaus = {
                "status": tilakoodi,
                "teksti": "Lentokenttää ei löytynyt"
            }
        else:
            tilakoodi = 200
            vastaus = {
                "ICAO": rivi[0],
                "Name": rivi[1],
                "Municipality": rivi[2]
            }
    except mysql.connector.Error:
        tilakoodi = 500
        vastaus = {
            "status": tilakoodi,
            "teksti": "Tietokantavirhe"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)