# cart.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data structure to store the cart items
cart_items = []

@app.route('/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id')

    # Filter cart items based on the user_id
    user_cart_items = [item for item in cart_items if item['user_id'] == user_id]

    return jsonify(user_cart_items)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    # Create a new cart item
    cart_item = {
        'user_id': user_id,
        'product_id': product_id
    }

    # Add the cart item to the cart_items list
    cart_items.append(cart_item)

    return jsonify({'message': 'Product added to cart'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


