# Chapter 24 - 주문별 매출 계산 열 만들기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

print(df[["order_id", "product", "price", "quantity", "sales_amount"]].head())
