import csv
import random
from datetime import datetime
import os

FILE_PATH = "data/cloud_cost_data.csv"
HEADER = ["timestamp", "cpu", "memory", "storage", "cost"]

def ensure_csv_header():
    """Ensure the CSV file exists and has the correct header."""
    if not os.path.exists(FILE_PATH):
        # File doesn’t exist → create with header
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)
    else:
        # File exists → check if header is correct
        with open(FILE_PATH, mode="r") as file:
            first_line = file.readline().strip().split(",")
        
        if first_line != HEADER:
            # If header mismatch → overwrite with correct header
            with open(FILE_PATH, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(HEADER)

def generate_record():
    """Generate one synthetic cloud cost record."""
    timestamp = datetime.now().isoformat()
    cpu = random.choice([1, 2, 4, 8])
    memory = random.choice([2, 4, 8, 16, 32])
    storage = random.choice([50, 100, 200, 400, 800])
    cost = round(cpu * 10 + memory * 5 + storage * 0.2 + random.uniform(-10, 10), 2)
    return [timestamp, cpu, memory, storage, cost]

if __name__ == "__main__":
    ensure_csv_header()
    record = generate_record()
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)
    print(f" Added record to {FILE_PATH}: {record}")
