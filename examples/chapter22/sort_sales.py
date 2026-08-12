# Chapter 22 - 판매 금액이 큰 기록부터 정렬하기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

sorted_df = df.sort_values("sales_amount", ascending=False)
print(sorted_df[["product", "category", "sales_amount"]].head())
