from .base_model import CSVModel

class AddressModel(CSVModel):
    """Manages data from addresses.csv"""
    def __init__(self):
        super().__init__('addresses')
        self.primary_key = 'AddressID'