from models.inventory_model import InventoryModel

class InventoryRepository:
    def __init__(self):
        self.db = InventoryModel()

    def get_stock_by_product_id(self, product_id):
        all_inventory = self.db.get_all()
        for record in all_inventory:
            if record['product_id'] == str(product_id):
                return record
        return None

    def get_quantity(self, product_id):
        record = self.get_stock_by_product_id(product_id)
        if record:
            return int(record.get('quantity_in_stock', 0))
        return 0

    def decrease_stock(self, product_id, quantity_sold):
        record = self.get_stock_by_product_id(product_id)
        if record:
            current_stock = int(record['quantity_in_stock'])
            new_stock = current_stock - quantity_sold
            print(f"Stock for product {product_id} reduced to {new_stock}")
            self.db.update(record['inventory_id'], {'quantity_in_stock': str(new_stock)})