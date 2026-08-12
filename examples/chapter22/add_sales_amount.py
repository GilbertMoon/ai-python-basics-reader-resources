# Chapter 22 - 판매 금액 열 만들기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

print(df[["product", "price", "quantity", "sales_amount"]].head())
