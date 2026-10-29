from flask import Flask, request, jsonify
app=Flask(__name__)
id=0
musicasdb=[]
@app.route("/musicas")
def mostrar():
    return jsonify(musicasdb)
@app.route("/musicas",methods=["POST"])
def addaluno():
    global id
    id=id+1
    dados=request.get_json()
    nome=dados.get("nome")
    artista=dados.get("artista")
    ano=dados.get("ano")
    musica={"id":id,"nome":nome,"artista":artista,"ano":ano}
    musicasdb.append(musica)
    return jsonify(musica)

@app.route("/musicas/<int:id>",methods=["PUT"])
def atualizar(id):
    dados=request.get_json()
    nome=dados.get("nome")
    artista=dados.get("artista")
    ano=dados.get("ano")
    for i in musicasdb:
        if i["id"]==id:
            i["nome"]=nome
            i["artista"]=artista
            i["ano"]=ano
            return jsonify({"atualizado":"Atualizei"})
    return jsonify({"NãoEncontrado":"NãoEncontrado"})

@app.route("/musicas/<int:id>",methods=["DELETE"])
def deletar(id):
    for i in musicasdb:
        if i["id"]==id:
            musicasdb.remove(i)
            return jsonify({"Removido":"removi"})
    return jsonify({"NãoEncontrado":"NãoEncontrado"})

app.run(debug=True)






















