from flask import Flask, redirect, url_for
from .controllers.user_controller import user_bp
from .controllers.product_controller import product_bp
from .controllers.cart_controller import cart_bp
from .controllers.order_controller import order_bp
from .controllers.api_controller import api_bp  

def create_app():
    app = Flask(__name__)
    

    app.secret_key = 'shopease_secret_key_123'

 
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(api_bp)  


    @app.after_request
    def add_header(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

 
    @app.route('/')
    def index():
        return redirect(url_for('product_routes.list_products'))

    return app