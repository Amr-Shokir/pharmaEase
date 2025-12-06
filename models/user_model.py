
from .base_model import CSVModel

class UserModel(CSVModel):
    """Manages data from users.csv"""
    def __init__(self):
        super().__init__('users')
        self.primary_key = 'user_id' # Explicitly set for clarity