# Chapter 16 - csv.reader로 CSV 읽기

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter16" / "sales.csv"

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
