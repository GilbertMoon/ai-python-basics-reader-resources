# Chapter 22 - 카테고리별 매출 합계 계산하기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

category_sales = (
    df.groupby("category")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)
