from flask import Flask, request, jsonify

app=Flask(__name__)

id=0
filmesdb=[]


@app.route("/filmes")
def mostrar():
    return jsonify(filmesdb)
        

@app.route("/filmes", methods=["POST"])
def addFilmes():
    global id
    id=id+1
    dados=request.get_json()
    nome=dados.get("nome")
    ano=dados.get("nome")
    diretor=dados.get("diretor")
    filme={"id":id,"nome":nome,"ano":ano,"diretor":diretor}
    filmesdb.append(filme)
    return jsonify(filme)


@app.route("/filmes/<int:id>",methods=["PUT"])
def editar(id):
    dados=request.get_json()
    nome=dados.get("nome")
    ano=dados.get("ano")
    diretor=dados.get("diretor")
    for i in filmesdb:
        if i["id"]==id:
            i["nome"]=nome
            i["ano"]=ano
            i["diretor"]=diretor
            return jsonify(i), 200
    return jsonify({"erro":"Não encontrado"}), 404

@app.route("/filmes/<int:id>",methods=["DELETE"])
def excluir(id):
    for i in filmesdb:
        if i["id"]==id:
            filmesdb.remove(i)
            return jsonify ({"removido":"Removi"})
    return jsonify({"erro":"Não encontrado"}), 404

app.run(debug=True)