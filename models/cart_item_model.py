
from .base_model import CSVModel


class CartItemModel(CSVModel):
    """Manages data from cart_items.csv"""
    def __init__(self):
        super().__init__('cart_items')
        self.primary_key = 'cart_item_id'