from flask import Flask, jsonify

app = Flask(__name__)

# Dados fictícios de times
times = [
    {"id": 1, "nome": "Flamengo", "cidade": "Rio de Janeiro", "titulos_brasileirao": 8},
    {"id": 2, "nome": "Corinthians", "cidade": "São Paulo", "titulos_brasileirao": 7},
    {"id": 3, "nome": "Palmeiras", "cidade": "São Paulo", "titulos_brasileirao": 12},
    {"id": 4, "nome": "Guarani de Juazeiro", "cidade": "Juazeiro do Norte", "titulos_brasileirao": 0}
]

@app.route("/")
def home():
    return jsonify({"mensagem": "API de Futebol - Consulte /times"})

@app.route("/times")
def get_times():
    return jsonify(times)

@app.route("/times/<int:time_id>")
def get_time(time_id):
    time = next((t for t in times if t["id"] == time_id), None)
    if time:
        return jsonify(time)
    return jsonify({"erro": "Time não encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
