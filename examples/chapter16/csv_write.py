# Chapter 16 - CSV 파일 쓰기

import csv
from pathlib import Path

output_path = Path(__file__).with_name("scores_output.csv")

rows = [
    ["name", "score"],
    ["민수", 85],
    ["지영", 92],
    ["서준", 78],
]

with open(output_path, "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("저장 위치:", output_path)
