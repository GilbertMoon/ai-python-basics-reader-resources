# Chapter 23 - 지출 데이터를 CSV로 저장하고 다시 불러오기

import csv
from pathlib import Path


output_path = Path(__file__).with_name("expenses_demo.csv")

expenses = [
    {"date": "2026-08-01", "category": "식비", "description": "점심", "amount": 12000},
    {"date": "2026-08-01", "category": "교통", "description": "버스", "amount": 1500},
    {"date": "2026-08-02", "category": "카페", "description": "커피", "amount": 4800},
]

fieldnames = ["date", "category", "description", "amount"]

with open(output_path, "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expenses)

loaded_expenses = []

with open(output_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["amount"] = int(row["amount"])
        loaded_expenses.append(row)

print("저장한 데이터:", expenses)
print("다시 읽은 데이터:", loaded_expenses)
print("같은 내용인가요?", expenses == loaded_expenses)
