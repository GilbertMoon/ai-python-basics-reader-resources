# Chapter 24 - 카테고리별 매출 질문에 답하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)
df["sales_amount"] = df["price"] * df["quantity"]

category_sales = (
    df.groupby("category")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

# idxmax()는 가장 큰 값이 있는 이름(인덱스)을 돌려줍니다.
top_category = category_sales.idxmax()
top_sales = category_sales.max()

print(category_sales)
print(f"\n가장 높은 카테고리: {top_category}")
print(f"매출: {top_sales:,}원")