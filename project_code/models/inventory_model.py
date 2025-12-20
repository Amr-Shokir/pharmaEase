
from .base_model import CSVModel

class InventoryModel(CSVModel):
    def __init__(self):
        super().__init__('inventory')
        self.primary_key = 'inventory_id'