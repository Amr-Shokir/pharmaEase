from models.order_model import OrderModel

class OrderRepository:
    def __init__(self):
        self.db = OrderModel()

    def create_order(self, user_id, shipping_address_id, subtotal, total_amount):
        new_order = {
            'user_id': user_id,
            'shipping_address_id': shipping_address_id,
            'subtotal': subtotal,
            'total_amount': total_amount,
            'order_status': 'Processing'
        }
        return self.db.create(new_order)

    def get_by_id(self, order_id):
        return self.db.find_by_id(order_id)