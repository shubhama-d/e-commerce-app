// app.js

// Fetch products and render the product listing
fetch('/products')
    .then(response => response.json())
    .then(products => {
        const productList = document.getElementById('product-list');
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.innerHTML = `<h3>${product.name}</h3><p>${product.price}</p>`;
            productList.appendChild(productElement);
        });
    });

// Fetch cart items and render the shopping cart
fetch('/cart?user_id=123')
    .then(response => response.json())
    .then(cartItems => {
        const cartItemsContainer = document.getElementById('cart-items');
        cartItems.forEach(cartItem => {
            const cartItemElement = document.createElement('div');
            cartItemElement.innerHTML = `<h3>${cartItem.product.name}</h3><p>${cartItem.product.price}</p>`;
            cartItemsContainer.appendChild(cartItemElement);
        });
    });

// Place order
function placeOrder() {
    const order = {
        user_id: '123',
        cart_items: []
    };

    // Fetch cart items and add them to the order
    fetch('/cart?user_id=123')
        .then(response => response.json())
        .then(cartItems => {
            order.cart_items = cartItems;
            
            // Send the order to the API gateway for processing
            fetch('/orders', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(order)
            })
            .then(response => response.json())
            .then(orderResponse => {
                // Handle the order response (e.g., display success message)
                console.log(orderResponse);
            });
        });
}
