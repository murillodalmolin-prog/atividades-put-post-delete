from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
cidadesdb = []

@app.route("/cidades", methods=["GET"])
def mostrar():
    return jsonify(cidadesdb)

@app.route("/cidades", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    cidade = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    cidadesdb.append(cidade)
    return jsonify(cidade)

@app.route("/cidades/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    for i in cidadesdb:
        if i["id"] == id:
            i["nome"] = nome
            i["preco"] = preco
            i["categoria"] = categoria
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/cidades/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in cidadesdb:
        if i["id"] == id:
            cidadesdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)