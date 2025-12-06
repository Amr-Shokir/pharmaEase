
from .base_model import CSVModel

class ProductModel(CSVModel):
    """Manages data from products.csv"""
    def __init__(self):
        super().__init__('products')
        self.primary_key = 'product_id'