from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
carrosdb = []

@app.route("/carros", methods=["GET"])
def mostrar():
    return jsonify(carrosdb)

@app.route("/carros", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")
    carro = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    carrosdb.append(carro)
    return jsonify(carro)

@app.route("/carros/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")
    for i in carrosdb:
        if i["id"] == id:
            i["modelo"] = modelo
            i["marca"] = marca
            i["ano"] = ano
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/carros/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in carrosdb:
        if i["id"] == id:
            carrosdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)