# Chapter 24 - 채널별·고객 유형별 매출 비교하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

channel_sales = (
    df.groupby("channel")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

customer_sales = (
    df.groupby("customer_type")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

print("=== 채널별 매출 ===")
print(channel_sales)

print("\n=== 고객 유형별 매출 ===")
print(customer_sales)

print("\n기존 고객과 신규 고객의 매출 차이:",
      f"{customer_sales['기존'] - customer_sales['신규']:,}원")
