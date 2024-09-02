from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/product', methods=['GET'])
def products():
    if request.method == 'GET':
        with open('static/product.json') as f:
            product = json.load(f)
        return jsonify(product)    
    
if __name__ == '__main__':
    app.run(debug=True)    