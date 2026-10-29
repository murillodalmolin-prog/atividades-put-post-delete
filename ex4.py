from flask import Flask, request, jsonify
app=Flask(__name__)
id=0
funcionariosdb=[]
@app.route("/funcionarios")
def mostrar():
    return jsonify(funcionariosdb)
@app.route("/funcionarios",methods=["POST"])
def adicionar():
    global id
    id=id+1
    dados=request.get_json()
    nome=dados.get("nome")
    cargo=dados.get("cargo")
    salario=dados.get("salario")
    func={"id":id,"nome":nome,"cargo":cargo,"salario":salario}
    funcionariosdb.append(func)
    return jsonify(func)

@app.route("/funcionarios/<int:id>",methods=["PUT"])
def atualizar(id):
    dados=request.get_json()
    nome=dados.get("nome")
    cargo=dados.get("cargo")
    salario=dados.get("salario")
    for i in funcionariosdb:
        if i["id"]==id:
            i["nome"]=nome
            i["cargo"]=cargo
            i["salario"]=salario
            return jsonify({"atualizado":"Atualizei"})
    return jsonify({"NãoEncontrado":"NãoEncontrado"})

@app.route("/funcionarios/<int:id>",methods=["DELETE"])
def deletar(id):
    for i in funcionariosdb:
        if i["id"]==id:
            funcionariosdb.remove(i)
            return jsonify({"Removido":"removi"})
    return jsonify({"NãoEncontrado":"NãoEncontrado"})

app.run(debug=True)