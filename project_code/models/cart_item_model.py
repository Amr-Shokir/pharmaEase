
from .base_model import CSVModel


class CartItemModel(CSVModel):
    def __init__(self):
        super().__init__('cart_items')
        self.primary_key = 'cart_item_id'