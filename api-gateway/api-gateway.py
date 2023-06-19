# api_gateway.py (API Gateway)

from flask import Flask, jsonify, request, send_from_directory
import requests

app = Flask(__name__)

# Product Service Endpoint
PRODUCT_SERVICE_URL = 'http://product-service:5001'

# Cart Service Endpoint
CART_SERVICE_URL = 'http://cart-service:5002'

# Order Service Endpoint
ORDER_SERVICE_URL = 'http://order-service:5003'

# Serve the frontend UI
@app.route('/', methods=['GET'])
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):
    return send_from_directory('frontend', path)

# Product Service routes
@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f'{PRODUCT_SERVICE_URL}/products')
    return jsonify(response.json())

# Cart Service routes
@app.route('/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id')
    response = requests.get(f'{CART_SERVICE_URL}/cart', params={'user_id': user_id})
    return jsonify(response.json())

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    response = requests.post(f'{CART_SERVICE_URL}/cart/add', json={'user_id': user_id, 'product_id': product_id})
    return jsonify(response.json())

# Order Service routes
@app.route('/orders', methods=['POST'])
def place_order():
    user_id = request.json.get('user_id')
    cart_items = request.json.get('cart_items')
    response = requests.post(f'{ORDER_SERVICE_URL}/orders', json={'user_id': user_id, 'cart_items': cart_items})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
