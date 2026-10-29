from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
produtosdb = []

@app.route("/Produtos", methods=["GET"])
def mostrar():
    return jsonify(produtosdb)

@app.route("/Produtos", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    prod = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    produtosdb.append(prod)
    return jsonify(prod)

@app.route("/Produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    for i in produtosdb:
        if i["id"] == id:
            i["nome"] = nome
            i["preco"] = preco
            i["categoria"] = categoria
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/Produtos/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in produtosdb:
        if i["id"] == id:
            produtosdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)