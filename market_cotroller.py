from flask import Flask, abort, jsonify, request, redirect, render_template
from dao_market import Market 

app = Flask(__name__)
market = Market() 

@app.route("/produtos", methods=['GET'])
def get_all_produtos():
    resp = jsonify(market.get_all())
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')
    
    return resp

@app.route("/produtos", methods=['POST'])
def create_produto():
    if not request.json or not 'code' in request.json:
        abort(400)
    
    produto = {
        'code': request.json.get("code", ""), 
        'name': request.json.get("name", ""), 
        'price': request.json.get("price", ""), 
        'quantity': request.json.get("quantity", ""), 
    }

    if (market.add_product(produto)):
        resp = jsonify(produto)
        resp.headers.set('Access-Control-Allow-Origin', '*')
        resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')
        return resp, 200
    else: 
        return jsonify({'response': False})

@app.route("/produtos/<string:codeProduto>", methods=['PUT'])
def put_product(codeProduto):

    check_product = list(filter(lambda product: product["code"] == codeProduto, market.get_all()))
    
    product = {
        'code': request.json.get("code", ""), 
        'name': request.json.get("name", ""), 
        'price': request.json.get("price", ""), 
        'quantity': request.json.get("quantity", ""), 
    }

    if (len(check_product) == 1):
        market.update_product(product)
        return jsonify(product), 200
    
    elif (len(check_product) == 0):
        market.add_product(product)
        return jsonify(product), 201
    
    else: 
        return jsonify({'response': False})

@app.route("/produtos/<string:codeProduto>", methods=['PATCH'])
def patch_product(codeProduto):

    check_product = list(filter(lambda product: product["code"] == codeProduto, market.get_all()))
    
    product = {
        'code': request.json.get("code", ""), 
        'name': request.json.get("name", ""), 
        'price': request.json.get("price", ""), 
        'quantity': request.json.get("quantity", ""), 
    }

    if (len(check_product) == 1):
        market.update_product(product)
        return jsonify(produto), 200
    
    elif (len(check_product) == 0):
        market.add_product(product)
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