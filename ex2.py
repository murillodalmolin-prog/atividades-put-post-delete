from flask import Flask, request, jsonify
app=Flask(__name__)
id=0
alunosdb=[]
@app.route("/alunos")
def mostrar():
    return jsonify(alunosdb)

@app.route("/alunos",methods=["POST"])
def addAluno():
    global id
    id=id+1
    dados=request.get_json()
    nome=dados.get("nome")
    curso=dados.get("curso")
    idade=dados.get("idade")
    aluno={"id":id,"nome":nome,"curso":curso,"idade":idade}
    alunosdb.append(aluno)
    return jsonify (aluno)

@app.route("/alunos/<int:id>",methods=["PUT"])
def editar(id):
    dados=request.get_json()
    nome=dados.get("nome")
    idade=dados.get("idade")
    curso=dados.get("curso")
    for i in alunosdb:
        if i["id"]==id:
            i["nome"]=nome
            i["idade"]=idade
            i["curso"]=curso
            return jsonify(i), 200
    return jsonify({"erro":"Não encontrado"}), 404

@app.route("/alunos/<int:id>",methods=["DELETE"])
def excluir(id):
    for i in alunosdb:
        if i["id"]==id:
            alunosdb.remove(i)
            return jsonify ({"removido":"Removi"})
    return jsonify({"erro":"Não encontrado"}), 404


app.run(debug=True)














