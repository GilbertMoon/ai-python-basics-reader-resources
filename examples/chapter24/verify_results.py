# Chapter 24 - 그룹별 결과와 전체 매출 검증하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

total_sales = df["sales_amount"].sum()
category_sales = df.groupby("category")["sales_amount"].sum()
channel_sales = df.groupby("channel")["sales_amount"].sum()
customer_sales = df.groupby("customer_type")["sales_amount"].sum()

print("전체 매출:", total_sales)
print("카테고리 합계:", category_sales.sum())
print("채널 합계:", channel_sales.sum())
print("고객 유형 합계:", customer_sales.sum())

print(total_sales == category_sales.sum())
print(total_sales == channel_sales.sum())
print(total_sales == customer_sales.sum())
