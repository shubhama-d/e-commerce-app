from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    product_service_url = 'http://product-service:5000/api/products'  # Assuming product service runs on port 5000
    response = requests.get(product_service_url)
    products = response.json()
    return jsonify(products)

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    cart_service_url = 'http://cart-service:5001/api/cart'  # Assuming cart service runs on port 5000
    product_id = request.json.get('product_id')
    user_id = request.json.get('user_id')
    payload = {'product_id': product_id, 'user_id': user_id}
    response = requests.post(cart_service_url, json=payload)
    return response.json()

if __name__ == '__main__':
    app.run()


