from flask import Flask, abort, jsonify, request, redirect, render_template
from dao_market import Market 

app = Flask(__name__)
market = Market() 

@app.route("/produtos", methods=['GET'])
def get_all_produtos():
    return jsonify(market.get_all())

@app.route("/produtos", methods=['POST'])
def create_produto():
    if not request.json or not 'code' in request.json:
        abort(400)
    
    produto = {
        'code': request.json['code'], 
        'name': request.json['name'], 
        'price': request.json['price'], 
        'quantity': request.json['quantity'], 
    }

    if (market.add_product(produto)):
        return jsonify({'produto': produto }), 201
    else: 
        return jsonify({'response': False})

@app.route("/produtos/<string:codeProduto>", methods=['DELETE'])
def remove_produto(codeProduto):
    if (not market.remove_product(codeProduto)):
        return jsonify({"response": False}) 

    return jsonify({"response": True}) 

if __name__ == "__main__":
    print("Servidor em execução!")
    app.run(host='0.0.0.0', debug=True)