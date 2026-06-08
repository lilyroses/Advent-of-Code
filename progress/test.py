import json


PROGRESS_DATA_FILE = "progress_data.json"
with open(PROGRESS_DATA_FILE, "r") as f:
    PROGRESS_DATA = json.load(f)



