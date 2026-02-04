import csv
import json
import os

def load_config(config_file_name = "config.json"):
  try:
    with open(config_file_name,'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return None
