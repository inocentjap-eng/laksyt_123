from flask import Flask
import math

app = Flask(__name__)
app.json.sort_keys = False   # keep keys in the order I write them


def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/alkuluku/<luku>")
def alkuluku(luku):
    try:
        n = int(luku)
    except ValueError:
        return {"status": 400, "teksti": "Parametrin on oltava kokonaisluku"}, 400

    return {"Number": n, "isPrime": is_prime(n)}


@app.errorhandler(404)
def page_not_found(error):
    return {"status": 404, "teksti": "Virheellinen päätepiste"}, 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)