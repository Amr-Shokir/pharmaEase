from models.address_model import AddressModel

class AddressRepository:
    def __init__(self):
        self.db = AddressModel()

    def get_by_user_id(self, user_id):
        all_addresses = self.db.get_all()
        return [a for a in all_addresses if a['user_id'] == str(user_id)]
    
    def create_address(self, address_data):
        return self.db.create(address_data)