import csv
import json
import os

def load_config(config_file_name = "config.json"):
  try:
    with open(config_file_name,'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return None

def load_data(csv_file_path):
  data = []
  if not os.path.exists(csv_file_path):
    return []

  try:
    with open(csv_file_path,mode = 'r',encoding='utf-8-sig') as f:
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

