# order.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data.get('user_id')
    cart_items = data.get('cart_items')

    # Process the order and generate an order ID
    order_id = 'ORDER-123'

    return jsonify({'order_id': order_id, 'message': 'Order placed successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
