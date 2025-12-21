
from .base_model import CSVModel

class UserModel(CSVModel):
    def __init__(self):
        super().__init__('users')
        self.primary_key = 'user_id' 


