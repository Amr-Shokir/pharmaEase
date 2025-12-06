from models.cart_model import CartModel

class CartRepository:
    def __init__(self):
        self.db = CartModel()

    def create_cart(self, user_id):
        """Creates a new cart for a user."""
        new_cart = {
            'user_id': user_id,
            'session_id': 'session_123', # simplified
            # created_at handled by DB or Model default
        }
        return self.db.create(new_cart)

    def get_active_cart_by_user(self, user_id):
        """Finds the most recent cart for a user."""
        # In a real app, you'd check if the cart is "checked out" or not.
        # For now, we return the last created cart for this user.
        all_carts = self.db.get_all()
        user_carts = [c for c in all_carts if c['user_id'] == str(user_id)]
        
        if user_carts:
            return user_carts[-1] # Return the last one
        return None