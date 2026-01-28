import json
import os
from pathlib import Path

def read_json(file_path: str):
    path = Path(file_path)
    if not path.exists():
        return []
    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_json(file_path: str, data):
    path = Path(file_path)
    # Automatically create the data folder if missing
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)