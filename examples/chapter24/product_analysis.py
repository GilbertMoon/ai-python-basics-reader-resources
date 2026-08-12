# Chapter 24 - 상품별 매출 순위 확인하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

product_sales = (
    df.groupby("product")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

print("=== 상품별 매출 상위 5개 ===")
print(product_sales.head())
