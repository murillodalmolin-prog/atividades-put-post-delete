from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
jogosdb = []

@app.route("/jogos", methods=["GET"])
def mostrar():
    return jsonify(jogosdb)

@app.route("/jogos", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    jogo = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogosdb.append(jogo)
    return jsonify(jogo)

@app.route("/jogos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    for i in jogosdb:
        if i["id"] == id:
            i["nome"] = nome
            i["genero"] = genero
            i["ano"] = ano
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/jogos/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in jogosdb:
        if i["id"] == id:
            jogosdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)