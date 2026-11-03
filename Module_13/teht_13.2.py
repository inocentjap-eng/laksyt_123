from flask import Flask
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "1234",
    "database": "flight_game",
    "use_pure": True,
}


def get_airport(icao):
    connection = mysql.connector.connect(**DB_CONFIG)
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ident, name, municipality FROM airport WHERE ident = %s",
            (icao,),
        )
        return cursor.fetchone()
    finally:
        connection.close()


@app.route("/kenttä/<icao>")
def kentta(icao):
    icao = icao.strip().upper()

    try:
        row = get_airport(icao)
    except mysql.connector.Error as e:
        print("DB ERROR:", e)
        return {"status": 500, "teksti": "Tietokantavirhe"}, 500

    if row is None:
        return {"status": 404, "teksti": "Lentokenttää ei löytynyt"}, 404

    return {"ICAO": row[0], "Name": row[1], "Municipality": row[2]}


@app.errorhandler(404)
def page_not_found(error):
    return {"status": 404, "teksti": "Virheellinen päätepiste"}, 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)