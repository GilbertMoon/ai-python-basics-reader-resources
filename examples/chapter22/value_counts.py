# Chapter 22 - 범주별 판매 기록 개수 확인하기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)

print("=== 카테고리별 기록 수 ===")
print(df["category"].value_counts())

print("\n=== 채널별 기록 수 ===")
print(df["channel"].value_counts())
