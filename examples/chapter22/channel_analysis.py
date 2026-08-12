# Chapter 22 - 채널별 판매 기록 수와 매출 비교하기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

print("=== 채널별 기록 수 ===")
print(df["channel"].value_counts())

print("\n=== 채널별 매출 ===")
print(df.groupby("channel")["sales_amount"].sum())
