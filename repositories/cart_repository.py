from models.cart_model import CartModel

class CartRepository:
    def __init__(self):
        self.db = CartModel()

    def create_cart(self, user_id):
        new_cart = {
            'user_id': user_id,
            'session_id': 'session_123', 
        }
        return self.db.create(new_cart)

    def get_active_cart_by_user(self, user_id):
        all_carts = self.db.get_all()
        user_carts = [c for c in all_carts if c['user_id'] == str(user_id)]
        
        if user_carts:
            return user_carts[-1] 
        return None