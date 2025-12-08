

from .base_model import CSVModel

class OrderItemModel(CSVModel):
    def __init__(self):
        super().__init__('order_items')
        self.primary_key = 'order_item_id'