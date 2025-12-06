import csv
import os

class CSVModel:
    def __init__(self, filename_prefix):
        self.filename_prefix = filename_prefix 
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', f'{filename_prefix}.csv')
        
        self.records = []
        self.primary_key = None 

        try:
            with open(data_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.records = list(reader)
                if reader.fieldnames:
                    self.primary_key = reader.fieldnames[0]
            print(f"Successfully loaded {len(self.records)} records from {filename_prefix}.csv")

        except FileNotFoundError:
            print(f"Warning: CSV file not found at {data_path}. Initializing with empty data.")
        except Exception as e:
            print(f"Error loading {filename_prefix}.csv: {e}")

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
        ids = [int(r[self.primary_key]) for r in self.records if r[self.primary_key].isdigit()]
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
        

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', f'{self.filename_prefix}.csv') 

        with open(data_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.records)