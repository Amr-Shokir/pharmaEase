from db_singleton import DatabaseHandler # Import the Singleton

class CSVModel:
    def __init__(self, filename_prefix):
        self.filename_prefix = filename_prefix 
        
        # USE SINGLETON: Get the single instance of the DB Handler
        self.db = DatabaseHandler()
        
        self.records = []
        self.primary_key = None 

        # Delegate file loading to the Singleton
        self.records, fieldnames = self.db.load_data(filename_prefix)
        
        if fieldnames:
            self.primary_key = fieldnames[0]

    def get_all(self):
        return self.records

    def find_by_id(self, record_id):
        if not self.primary_key:
            return None
        target_id_str = str(record_id)
        for record in self.records:
            if record.get(self.primary_key) == target_id_str:
                return record
        return None
    
    def generate_id(self):
        if not self.records:
            return 1
        # Filter out empty or malformed IDs just in case
        ids = [int(r[self.primary_key]) for r in self.records if r.get(self.primary_key, '').isdigit()]
        return max(ids) + 1 if ids else 1

    def create(self, new_record):
        new_id = self.generate_id()
        new_record[self.primary_key] = str(new_id)
        self.records.append(new_record)
        self.save_to_file()
        return new_record

    def update(self, record_id, updated_fields):
        if not self.primary_key:
            return False
        target_id_str = str(record_id)
        record_found = False

        for record in self.records:
            if record.get(self.primary_key) == target_id_str:
                record.update(updated_fields)
                record_found = True
                break
        
        if record_found:
            self.save_to_file()
            return True
        return False    

    def delete(self, record_id):
        if not self.primary_key:
            return False
        target_id_str = str(record_id)
        initial_count = len(self.records)
        self.records = [r for r in self.records if r.get(self.primary_key) != target_id_str]
        
        if len(self.records) < initial_count:
            self.save_to_file()
            return True
        return False
            
    def save_to_file(self):
        if not self.records:
            return
        fieldnames = list(self.records[0].keys())
        
        # USE SINGLETON: Delegate saving to the Singleton
        self.db.save_data(self.filename_prefix, self.records, fieldnames)