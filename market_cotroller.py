from flask import Flask, jsonify, request, redirect, render_template
from dao_market import Market 

app = Flask(__name__)

@app.route("/produtos", methods=['GET'])
def get_all_produtos():
    market = Market() 

    return jsonify(market.get_all())

if __name__ == "__main__":
    print("Servidor em execução!")
    app.run(host='0.0.0.0', debug=True)