from flask import Blueprint, render_template, request
from repositories.product_repository import ProductRepository 


product_bp = Blueprint('product_routes', __name__, url_prefix='/')

product_repo = ProductRepository()



@product_bp.route('/')
@product_bp.route('/products')
def list_products():
    category = request.args.get('category')
    search_term = request.args.get('q')

    if category:
        products = product_repo.get_by_category(category) 
    elif search_term:
        products = product_repo.search_products(search_term) 
    else:
        products = product_repo.get_all() 

    
    return render_template('product/catalog.html', 
                           products=products, 
                           current_category=category)


@product_bp.route('/product/<int:product_id>')
def view_product(product_id):
    product = product_repo.get_by_id(product_id)
    
    if not product:
        return "Product Not Found", 404

    
    return render_template('product/detail.html', 
                           product=product) 
    