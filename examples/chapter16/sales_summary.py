# Chapter 16 - CSV 매출 데이터 요약

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter16" / "sales.csv"

total_sales = 0
total_quantity = 0
row_count = 0

with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = int(row["price"])
        quantity = int(row["quantity"])
        amount = price * quantity

        total_sales += amount
        total_quantity += quantity
        row_count += 1

        if amount >= 100000:
            print(f"고매출 항목: {row['product']} - {amount:,}원")

average_per_item = total_sales / total_quantity

print(f"기록 건수: {row_count}건")
print(f"총 판매 수량: {total_quantity}개")
print(f"총 매출: {total_sales:,}원")
print(f"상품 1개당 평균 매출: {average_per_item:,.0f}원")
