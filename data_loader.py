import csv
import os
import json

def load_config(config_file="config.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, config_file)

    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception:
            return None

def load_data(csv_file_path):
    if not os.path.isabs(csv_file_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(script_dir, csv_file_path)

    if not os.path.exists(csv_file_path):
        return []

    try:
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            
            data = [
                {
                    "Country Name": row.get("Country Name", row.get("Country", "Unknown")),
                    "Region": row.get("Continent", row.get("Region", "Unknown")),
                    "Year": int(year_key),
                    "Value": float(value)
                }
                for row in reader
                for year_key, value in row.items()
                if year_key.isdigit() and value.strip()
            ]
            
            return data

    except Exception:
        return []
