from models.cart_item_model import CartItemModel

class CartItemRepository:
    def __init__(self):
        self.db = CartItemModel()

    def get_items_by_cart_id(self, cart_id):
        all_items = self.db.get_all()
        return [item for item in all_items if item['cart_id'] == str(cart_id)]

    def add_item(self, cart_id, product_id, quantity):
        existing_items = self.get_items_by_cart_id(cart_id)
        for item in existing_items:
            if item['product_id'] == str(product_id):
                return item

        new_item = {
            'cart_id': cart_id,
            'product_id': product_id,
            'quantity': quantity
        }
        return self.db.create(new_item)

    def delete_items_by_cart_id(self, cart_id):
        items = self.get_items_by_cart_id(cart_id)
        for item in items:
            self.db.delete(item['cart_item_id'])
    
    def delete_item(self, item_id):
        self.db.delete(item_id)