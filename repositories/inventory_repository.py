from models.inventory_model import InventoryModel

class InventoryRepository:
    def __init__(self):
        self.db = InventoryModel()

    def get_stock_by_product_id(self, product_id):
        """
        Finds the inventory record for a specific product.
        Returns the record (dict) or None if not found.
        """
        all_inventory = self.db.get_all()
        # Search for the record matching the product_id
        for record in all_inventory:
            if record['product_id'] == str(product_id):
                return record
        return None

    def get_quantity(self, product_id):
        """
        Helper to just get the number of items in stock.
        Returns 0 if no record exists.
        """
        record = self.get_stock_by_product_id(product_id)
        if record:
            return int(record.get('quantity_in_stock', 0))
        return 0

    def decrease_stock(self, product_id, quantity_sold):
        """
        Decreases the stock for a product.
        (Note: Requires an 'update' method in the base CSVModel to persist changes)
        """
        record = self.get_stock_by_product_id(product_id)
        if record:
            current_stock = int(record['quantity_in_stock'])
            new_stock = current_stock - quantity_sold
            
            # Here you would call a method to save this change back to the CSV
            # For example: self.db.update(record['inventory_id'], {'quantity_in_stock': new_stock})
            # For this demo, we just print the action
            print(f"Stock for product {product_id} reduced to {new_stock}")