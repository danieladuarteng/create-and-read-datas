from flask import Flask, render_template, request, url_for, redirect,jsonify,json,request

from pymongo import MongoClient

#conexão bd
app = Flask(__name__)
conexao = MongoClient('localhost',27017)
db = conexao['teste_db']

#inserindo contatos iniciais
contato1 = {'nome': 'Lucas', 'email': 'lucas@gmail.com', 'telefone': '11 99389-3244'}
contato2 = {'nome': 'Lara', 'email': 'lara@gmail.com', 'telefone': '11 99333-3556'}
catalogo = db.catalogo
catalogo.insert_one(contato1)
catalogo.insert_one(contato2)


#página inicial
@app.route('/')
def showMachineList():
    return render_template('list.html')

@app.route("/insert_records", methods=['POST'])
def insert_records():
    
        json_data = request.json['info']
        nome = json_data['nome']
        email = json_data['email']
        telefone = json_data['telefone']

        db.catalogo.insert_one({
            'nome':nome,'email':email,'telefone':telefone
            })
      
        return jsonify(status='OK',message='inserted successfully')

@app.route('/get_records',methods=['POST'])
def get_records():
  
    contatos = db.catalogo.find()  

    return render_template('list.html',contatos=contatos)


if __name__ == "__main__":
    app.run(debug=True)