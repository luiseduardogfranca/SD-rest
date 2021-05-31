from flask import Flask, abort, jsonify, request, redirect, render_template
from dao_market import Market 

app = Flask(__name__)
market = Market() 

@app.route("/produtos", methods=['GET'])
def get_all_produtos():
    return jsonify(market.get_all())

@app.route("/produtos", methods=['POST'])
def create_produto():
    print(request.json)
    if not request.json or not 'code' in request.json:
        abort(400)
    
    produto = {
        'code': request.json.get("code", ""), 
        'name': request.json.get("name", ""), 
        'price': request.json.get("price", ""), 
        'quantity': request.json.get("quantity", ""), 
    }

    if (market.add_product(produto)):
        return jsonify(produto), 201
    else: 
        return jsonify({'response': False})

@app.route("/produtos/<string:codeProduto>", methods=['DELETE'])
def remove_produto(codeProduto):
    if (not market.remove_product(codeProduto)):
        abort(404) 

    return jsonify({"response": True}), 200 

if __name__ == "__main__":
    print("Servidor em execução!")
    app.run(host='127.0.0.1', debug=True)