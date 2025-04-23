from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Abilita i CORS per tutte le origini

@app.route("/astroseek", methods=["GET"])
def get_mock_data():
    nome = request.args.get("nome")
    return jsonify({
        "ascendente": "Vergine",
        "luna": "Scorpione",
        "sole": "Acquario",
        "nome": nome
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
