from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.order_repository import OrderRepository
from repositories.order_item_repository import OrderItemRepository
from repositories.cart_repository import CartRepository
from repositories.cart_item_repository import CartItemRepository
from repositories.product_repository import ProductRepository
from repositories.address_repository import AddressRepository # Needed for shipping

order_bp = Blueprint('order_routes', __name__, url_prefix='/order')

# Initialize Repositories
order_repo = OrderRepository()
order_item_repo = OrderItemRepository()
cart_repo = CartRepository()
cart_item_repo = CartItemRepository()
product_repo = ProductRepository()
address_repo = AddressRepository()

@order_bp.route('/checkout', methods=['GET'])
def checkout():
    """Displays the checkout page with order summary and address selection."""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_routes.login'))

    # 1. Get Cart Logic (Similar to view_cart)
    cart = cart_repo.get_active_cart_by_user(user_id)
    if not cart:
        return redirect(url_for('product_routes.list_products'))

    cart_items = cart_item_repo.get_items_by_cart_id(cart['cart_id'])
    
    if not cart_items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for('product_routes.list_products'))

    # Calculate Subtotal
    subtotal = 0
    for item in cart_items:
        product = product_repo.get_by_id(item['product_id'])
        if product:
            subtotal += int(item['quantity']) * float(product['price'])

    # 2. Get User Addresses for selection
    addresses = address_repo.get_by_user_id(user_id)

    return render_template('order/checkout.html', 
                           subtotal=subtotal, 
                           addresses=addresses,
                           shipping_cost=10.00) # Hardcoded shipping for demo


@order_bp.route('/place', methods=['POST'])
def place_order():
    """Handles the final order creation."""
    user_id = session.get('user_id')
    shipping_address_id = request.form.get('address_id')
    
    # 1. Retrieve Cart Data Again (Security check)
    cart = cart_repo.get_active_cart_by_user(user_id)
    cart_items = cart_item_repo.get_items_by_cart_id(cart['cart_id'])
    
    # 2. Calculate Finals
    subtotal = 0
    items_to_order = [] # Store data to move to order_items
    
    for item in cart_items:
        product = product_repo.get_by_id(item['product_id'])
        qty = int(item['quantity'])
        price = float(product['price'])
        subtotal += qty * price
        
        items_to_order.append({
            'product_id': item['product_id'],
            'quantity': qty,
            'price_at_purchase': price
        })

    total_amount = subtotal + 10.00 # + Shipping

    # 3. Create Order Record
    new_order = order_repo.create_order(
        user_id=user_id,
        shipping_address_id=shipping_address_id,
        subtotal=subtotal,
        total_amount=total_amount
    )
    
    # 4. Create Order Items & Clear Cart
    # (In a real DB, this would be a transaction)
    order_id = new_order['order_id']
    
    for item in items_to_order:
        order_item_repo.create_order_item(
            order_id=order_id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price_at_purchase']
        )
        
    # 5. Clear the Cart Items
    # Depending on implementation, you might delete the cart or just the items
    cart_item_repo.delete_items_by_cart_id(cart['cart_id'])

    return redirect(url_for('order_routes.confirmation', order_id=order_id))


@order_bp.route('/confirmation/<int:order_id>')
def confirmation(order_id):
    """Shows the receipt."""
    order = order_repo.get_by_id(order_id)
    return render_template('order/confirmation.html', order=order)