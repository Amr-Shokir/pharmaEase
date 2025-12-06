

from .base_model import CSVModel

class CartModel(CSVModel):
    def __init__(self):
        super().__init__('carts')
        self.primary_key = 'cart_id'