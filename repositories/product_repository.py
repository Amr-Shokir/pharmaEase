from models.product_model import ProductModel

class ProductRepository:
    def __init__(self):
        self.db = ProductModel()

    def get_all(self):
        return self.db.get_all()

    def get_by_id(self, product_id):
        return self.db.find_by_id(product_id)

    def get_by_category(self, category):
        all_products = self.db.get_all()
        # List comprehension to filter
        return [p for p in all_products if p.get('category') == category]

    def search_products(self, query):
        all_products = self.db.get_all()
        query = query.lower()
        return [
            p for p in all_products 
            if query in p.get('name', '').lower() or query in p.get('description', '').lower()
        ]
    
    def search_products(self, query):
        all_products = self.db.get_all()
        query = query.lower()
        return [
            p for p in all_products 
            if query in p.get('name', '').lower() 
            or query in p.get('description', '').lower()
            or query in p.get('category', '').lower()  # <-- ADDED THIS LINE
        ]