# Chapter 21 - 판매 데이터 첫 점검 보고서

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter21" / "store_sales.csv"

df = pd.read_csv(file_path)

print("=== 데이터 기본 정보 ===")
print("크기:", df.shape)
print("열:", list(df.columns))

print("\n=== 앞쪽 데이터 ===")
print(df.head())

print("\n=== 결측값 ===")
print(df.isna().sum())

print("\n=== 가격 요약 ===")
print("평균 가격:", df["price"].mean())
print("최저 가격:", df["price"].min())
print("최고 가격:", df["price"].max())
print("판매 수량 합계:", df["quantity"].sum())

print("\n=== 5만원 이상 상품 ===")
print(df[df["price"] >= 50000][["product", "price"]])
