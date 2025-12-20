from flask import Blueprint, render_template, request
from ..repositories.product_repository import ProductRepository 
from ..repositories.inventory_repository import InventoryRepository
import math

product_bp = Blueprint('product_routes', __name__, url_prefix='/')

PRODUCTS_PER_PAGE = 12  # 3 rows * 4 items = 12

product_repo = ProductRepository()
inventory_repo = InventoryRepository()


@product_bp.route('/')
@product_bp.route('/products')
def list_products():
    category = request.args.get('category')
    search_term = request.args.get('q')
    
    page = request.args.get('page', 1, type=int)

    if category:
        all_products = product_repo.get_by_category(category) 
    elif search_term:
        all_products = product_repo.search_products(search_term) 
    else:
        all_products = product_repo.get_all() 

    total_products = len(all_products)
    total_pages = math.ceil(total_products / PRODUCTS_PER_PAGE)

    if page < 1: page = 1
    if page > total_pages and total_pages > 0: page = total_pages

    start = (page - 1) * PRODUCTS_PER_PAGE
    end = start + PRODUCTS_PER_PAGE
    paginated_products = all_products[start:end]

    return render_template('product/catalog.html', 
                           products=paginated_products, 
                           current_category=category,
                           current_q=search_term,
                           page=page,
                           total_pages=total_pages)


@product_bp.route('/product/<int:product_id>')
def view_product(product_id):
    product = product_repo.get_by_id(product_id)
    
    if not product:
        return "Product Not Found", 404

    stock_record = inventory_repo.get_stock_by_product_id(product_id)
    quantity = int(stock_record['quantity_in_stock']) if stock_record else 0
    
    return render_template('product/detail.html', 
                           product=product, 
                           quantity=quantity)
    