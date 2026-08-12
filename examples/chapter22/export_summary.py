# Chapter 22 - 카테고리별 매출 요약을 CSV로 저장하기

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter22" / "store_sales.csv"
output_path = Path(__file__).with_name("category_sales_summary.csv")

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

category_summary = (
    df.groupby("category", as_index=False)["sales_amount"]
      .sum()
      .sort_values("sales_amount", ascending=False)
)

category_summary.to_csv(output_path, index=False, encoding="utf-8-sig")
print(category_summary)
print("저장 위치:", output_path)
