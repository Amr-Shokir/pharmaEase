
from flask import Flask, render_template, request, redirect, url_for

# Import all models
from models.user_model import UserModel
from models.product_model import ProductModel
from models.cart_model import CartModel, CartItemModel
from models.order_model import OrderModel, OrderItemModel
from models.address_model import AddressModel
from models.inventory_model import InventoryModel

app = Flask(__name__)


user_db = UserModel()
product_db = ProductModel()
cart_db = CartModel()
cart_item_db = CartItemModel()
order_db = OrderModel()
order_item_db = OrderItemModel()
address_db = AddressModel()
inventory_db = InventoryModel()


