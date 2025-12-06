
from .base_model import CSVModel

class OrderModel(CSVModel):
    """Manages data from orders.csv"""
    def __init__(self):
        super().__init__('orders')
        self.primary_key = 'order_id'