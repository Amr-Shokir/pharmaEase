from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.order_repository import OrderRepository
from repositories.order_item_repository import OrderItemRepository
from repositories.cart_repository import CartRepository
from repositories.cart_item_repository import CartItemRepository
from repositories.product_repository import ProductRepository
from repositories.inventory_repository import InventoryRepository
from repositories.address_repository import AddressRepository 

order_bp = Blueprint('order_routes', __name__, url_prefix='/order')

# Initialize Repositories
order_repo = OrderRepository()
order_item_repo = OrderItemRepository()
cart_repo = CartRepository()
cart_item_repo = CartItemRepository()
product_repo = ProductRepository()
address_repo = AddressRepository()
inventory_repo = InventoryRepository()


@order_bp.route('/checkout', methods=['GET'])
def checkout():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_routes.login'))

    cart = cart_repo.get_active_cart_by_user(user_id)
    if not cart:
        return redirect(url_for('product_routes.list_products'))

    cart_items = cart_item_repo.get_items_by_cart_id(cart['cart_id'])
    
    if not cart_items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for('product_routes.list_products'))

    subtotal = 0
    for item in cart_items:
        product = product_repo.get_by_id(item['product_id'])
        if product:
            subtotal += int(item['quantity']) * float(product['price'])

    addresses = address_repo.get_by_user_id(user_id)

    return render_template('order/checkout.html', 
                           subtotal=subtotal, 
                           addresses=addresses,
                           shipping_cost=10.00) 


@order_bp.route('/place', methods=['POST'])
def place_order():
    user_id = session.get('user_id')
    shipping_address_id = request.form.get('address_id')
    
    cart = cart_repo.get_active_cart_by_user(user_id)
    cart_items = cart_item_repo.get_items_by_cart_id(cart['cart_id'])
    
    subtotal = 0
    items_to_order = [] 
    
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


    new_order = order_repo.create_order(
        user_id=user_id,
        shipping_address_id=shipping_address_id,
        subtotal=subtotal,
        total_amount=total_amount
    )
    
    order_id = new_order['order_id']
    
    for item in items_to_order:
        order_item_repo.create_order_item(
            order_id=order_id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price_at_purchase']
        )
    cart_item_repo.delete_items_by_cart_id(cart['cart_id'])
    inventory_repo.decrease_stock(item['product_id'], item['quantity'])

    return redirect(url_for('order_routes.confirmation', order_id=order_id))


@order_bp.route('/confirmation/<int:order_id>')
def confirmation(order_id):
    order = order_repo.get_by_id(order_id)
    return render_template('order/confirmation.html', order=order)