from .base_model import CSVModel

class AddressModel(CSVModel):
    def __init__(self):
        super().__init__('addresses')
        self.primary_key = 'AddressID'