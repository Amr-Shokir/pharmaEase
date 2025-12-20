from ..models.order_item_model import OrderItemModel

class OrderItemRepository:
    def __init__(self):
        self.db = OrderItemModel()

    def create_order_item(self, order_id, product_id, quantity, price_at_purchase):
        item = {
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'price_at_purchase': price_at_purchase
        }
        return self.db.create(item)

    def get_items_by_order_id(self, order_id):
        all_items = self.db.get_all()
        return [i for i in all_items if i['order_id'] == str(order_id)]