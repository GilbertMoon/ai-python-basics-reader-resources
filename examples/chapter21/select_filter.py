# Chapter 21 - 열 선택과 조건 필터링

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter21" / "store_sales.csv"

df = pd.read_csv(file_path)

print("=== 상품과 가격 ===")
print(df[["product", "price"]])

print("\n=== 50,000원 이상 ===")
print(df[df["price"] >= 50000][["product", "price", "channel"]])

print("\n=== 온라인이면서 50,000원 이상 ===")
condition = (df["price"] >= 50000) & (df["channel"] == "온라인")
print(df[condition][["product", "price", "channel"]])
