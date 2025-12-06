
from flask import Flask, render_template, request, redirect, url_for

# Import all models
from models.user_model import UserModel
from models.product_model import ProductModel
from models.cart_model import CartModel, CartItemModel
from models.order_model import OrderModel, OrderItemModel
from models.address_model import AddressModel
from models.inventory_model import InventoryModel


# import all controllers
from controllers.user_controller import user_bp
from controllers.product_controller import product_bp
from controllers.cart_controller import cart_bp
from controllers.order_controller import order_bp

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Register Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(order_bp)


# user_db = UserModel()
# product_db = ProductModel()
# cart_db = CartModel()
# cart_item_db = CartItemModel()
# order_db = OrderModel()
# order_item_db = OrderItemModel()
# address_db = AddressModel()
# inventory_db = InventoryModel()


@app.route('/')
def index():
    return redirect(url_for('product_routes.list_products'))

if __name__ == '__main__':
    app.run(debug=True)