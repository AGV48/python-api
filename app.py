from flask import Flask, jsonify, abort

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)

@app.route("/<str:nombre>", methods=["GET"])
def Saludo(nombre):
    return jsonify(f"Hola {nombre}")

@app.route("/conteo", methods=["GET"])
def conteo(numero):
    numeros = []
    for i in range(numero):
        numeros.append(i)
    return jsonify(numeros)

@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201



if __name__ == "__main__":
    app.run(debug=True)
