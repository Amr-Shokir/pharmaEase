from flask import Blueprint, jsonify
from ..repositories.product_repository import ProductRepository

# We set url_prefix='/api', so all routes here will start with /api
api_bp = Blueprint('api_routes', __name__, url_prefix='/api')

@api_bp.route('/products', methods=['GET'])
def get_all_products():
    """
    Returns a JSON list of all products.
    Perfect for Android/Mobile consumption.
    """
    try:
        repo = ProductRepository()
        products = repo.get_all()
        
        # Convert Python Objects -> JSON Dictionary
        products_json = []
        for product in products:
            products_json.append({
                'id': getattr(product, 'product_id', 'N/A'), # Safety: uses 'N/A' if field missing
                'name': getattr(product, 'name', 'Unknown'),
                'price': getattr(product, 'price', 0.0),
                'description': getattr(product, 'description', ''),
                'image': getattr(product, 'image', '')
            })
            
        return jsonify(products_json), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500