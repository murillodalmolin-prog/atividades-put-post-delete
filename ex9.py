from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
restaurantesdb = []

@app.route("/restaurantes", methods=["GET"])
def mostrar():
    return jsonify(restaurantesdb)

@app.route("/restaurantes", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")
    restaurante = {"id": id, "nome": nome, "tipo": tipo, "cidade": cidade}
    restaurantesdb.append(restaurante)
    return jsonify(restaurante)

@app.route("/restaurantes/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")
    for i in restaurantesdb:
        if i["id"] == id:
            i["nome"] = nome
            i["tipo"] = tipo
            i["cidade"] = cidade
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/restaurantes/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in restaurantesdb:
        if i["id"] == id:
            restaurantesdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)