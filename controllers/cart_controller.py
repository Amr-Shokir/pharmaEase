from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.cart_repository import CartRepository
from repositories.cart_item_repository import CartItemRepository
from repositories.product_repository import ProductRepository

cart_bp = Blueprint('cart_routes', __name__, url_prefix='/cart')


cart_repo = CartRepository()
cart_item_repo = CartItemRepository()
product_repo = ProductRepository()

@cart_bp.route('/')
def view_cart():

    user_id = session.get('user_id')
    

    if not user_id:
        flash("Please log in to view your cart.", "warning")
        return redirect(url_for('user_routes.login'))


    cart = cart_repo.get_active_cart_by_user(user_id)
    if not cart:
        cart = cart_repo.create_cart(user_id)


    cart_items = cart_item_repo.get_items_by_cart_id(cart['cart_id'])
    

    cart_total = 0
    enriched_items = []
    
    for item in cart_items:
        product = product_repo.get_by_id(item['product_id'])
        if product:
            quantity = int(item['quantity'])
            price = float(product['price'])
            total_price = quantity * price
            cart_total += total_price
            
            enriched_items.append({
                'item_id': item['cart_item_id'],
                'product': product,
                'quantity': quantity,
                'total_price': total_price
            })

    return render_template('cart/view.html', cart_items=enriched_items, total=cart_total)


@cart_bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):

    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_routes.login'))

    quantity = int(request.form.get('quantity', 1))


    cart = cart_repo.get_active_cart_by_user(user_id)
    if not cart:
        cart = cart_repo.create_cart(user_id)


    cart_item_repo.add_item(cart['cart_id'], product_id, quantity)
    
    flash("Item added to cart!", "success")
    return redirect(url_for('cart_routes.view_cart'))


@cart_bp.route('/remove/<int:item_id>')
def remove_item(item_id):
    """Removes a specific item from the cart."""
    cart_item_repo.delete_item(item_id)
    return redirect(url_for('cart_routes.view_cart'))