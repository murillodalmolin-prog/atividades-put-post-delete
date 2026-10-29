from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
cursosdb = []

@app.route("/cursos", methods=["GET"])
def mostrar():
    return jsonify(cursosdb)

@app.route("/cursos", methods=["POST"])
def adicionar():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    restaurante = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    cursosdb.append(restaurante)
    return jsonify(restaurante)

@app.route("/cursos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    for i in cursosdb:
        if i["id"] == id:
            i["nome"] = nome
            i["instituicao"] = instituicao
            i["duracao"] = duracao
            return jsonify({"atualizado": "Atualizei"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

@app.route("/cursos/<int:id>", methods=["DELETE"])
def deletar(id):
    for i in cursosdb:
        if i["id"] == id:
            cursosdb.remove(i)
            return jsonify({"Removido": "removi"})
    return jsonify({"NãoEncontrado": "NãoEncontrado"})

app.run(debug=True)