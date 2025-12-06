from models.cart_item_model import CartItemModel

class CartItemRepository:
    def __init__(self):
        self.db = CartItemModel()

    def get_items_by_cart_id(self, cart_id):
        """Returns all items belonging to a specific cart."""
        all_items = self.db.get_all()
        return [item for item in all_items if item['cart_id'] == str(cart_id)]

    def add_item(self, cart_id, product_id, quantity):
        """Adds an item or updates quantity if it exists."""
        # 1. Check if item already exists in this cart
        existing_items = self.get_items_by_cart_id(cart_id)
        for item in existing_items:
            if item['product_id'] == str(product_id):
                # Update logic would go here (requires an update method in Model)
                # For simplicity in this CSV demo, we'll just return existing
                return item

        # 2. Create new item
        new_item = {
            'cart_id': cart_id,
            'product_id': product_id,
            'quantity': quantity
        }
        return self.db.create(new_item)

    def delete_items_by_cart_id(self, cart_id):
        """Removes all items for a cart (used after checkout)."""
        # Note: Implementing delete in CSV is harder (rewrite file), 
        # so for this demo we might skip it or you need to add delete logic to Base Model.
        pass
    
    def delete_item(self, item_id):
        """Removes a single item."""
        pass