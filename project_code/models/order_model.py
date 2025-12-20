
from .base_model import CSVModel

class OrderModel(CSVModel):
    def __init__(self):
        super().__init__('orders')
        self.primary_key = 'order_id'