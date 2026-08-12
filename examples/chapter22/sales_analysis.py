# Chapter 22 - 종합 실습: 판매 데이터 분석 보고서

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)

print("=== 데이터 점검 ===")
print("크기:", df.shape)
print("결측값:")
print(df.isna().sum())

df["sales_amount"] = df["price"] * df["quantity"]

print("\n=== 전체 요약 ===")
print(f"총 매출: {df['sales_amount'].sum():,}원")
print(f"평균 판매 금액: {df['sales_amount'].mean():,.0f}원")

print("\n=== 카테고리별 매출 ===")
category_sales = df.groupby("category")["sales_amount"].sum().sort_values(ascending=False)
print(category_sales)

print("\n=== 채널별 매출 ===")
channel_sales = df.groupby("channel")["sales_amount"].sum().sort_values(ascending=False)
print(channel_sales)

print("\n=== 100,000원 이상 판매 기록 ===")
high_sales = df[df["sales_amount"] >= 100000]
print(high_sales[["product", "category", "channel", "sales_amount"]].sort_values("sales_amount", ascending=False))
