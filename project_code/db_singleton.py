import os
import csv

class DatabaseHandler:
    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(DatabaseHandler, cls).__new__(cls)
            cls._instance.base_dir = os.path.dirname(os.path.abspath(__file__))
            print("--- Database Handler Singleton Initialized ---")
        return cls._instance

    def load_data(self, filename_prefix):
        
        data_path = os.path.join(self.base_dir, 'data', f'{filename_prefix}.csv')
        records = []
        fieldnames = None
        
        try:
            with open(data_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                records = list(reader)
                fieldnames = reader.fieldnames
            
        except FileNotFoundError:
            print(f"Warning: {filename_prefix}.csv not found.")
        except Exception as e:
            print(f"Error loading {filename_prefix}: {e}")
            
        return records, fieldnames

    def save_data(self, filename_prefix, records, fieldnames):

        if not records:
            return

        data_path = os.path.join(self.base_dir, 'data', f'{filename_prefix}.csv')
        
        
        if not fieldnames and records:
            fieldnames = list(records[0].keys())

        try:
            with open(data_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(records)
        except Exception as e:
            print(f"Error saving {filename_prefix}: {e}")