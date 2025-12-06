from flask import Flask, redirect, url_for

# Import the Blueprints (Controllers) we created
from controllers.user_controller import user_bp
from controllers.product_controller import product_bp
from controllers.cart_controller import cart_bp
from controllers.order_controller import order_bp

app = Flask(__name__)

app.secret_key = 'shopease_secret_key_123'


app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(order_bp)


@app.route('/')
def index():
    return redirect(url_for('product_routes.list_products'))

if __name__ == '__main__':
    app.run(debug=True)