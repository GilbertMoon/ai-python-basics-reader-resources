# Chapter 24 - 종합 프로젝트: 주문 데이터 미니 분석 보고서

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)

print("=== 1. 데이터 점검 ===")
print("크기:", df.shape)
print("결측값:")
print(df.isna().sum())

df["sales_amount"] = df["price"] * df["quantity"]

total_sales = df["sales_amount"].sum()

category_sales = (
    df.groupby("category")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

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

product_sales = (
    df.groupby("product")["sales_amount"]
      .sum()
      .sort_values(ascending=False)
)

# idxmax()는 가장 큰 값이 있는 이름(인덱스)을 돌려줍니다.
top_category = category_sales.idxmax()
top_channel = channel_sales.idxmax()
top_customer = customer_sales.idxmax()
top_product = product_sales.idxmax()

print("\n=== 2. 핵심 결과 ===")
print(f"전체 매출: {total_sales:,}원")
print(f"최고 매출 카테고리: {top_category} ({category_sales.max():,}원)")
print(f"최고 매출 채널: {top_channel} ({channel_sales.max():,}원)")
print(f"최고 매출 고객 유형: {top_customer} ({customer_sales.max():,}원)")
print(f"최고 매출 상품: {top_product} ({product_sales.max():,}원)")

print("\n=== 3. 합계 검증 ===")
print("카테고리 합계 일치:", total_sales == category_sales.sum())
print("채널 합계 일치:", total_sales == channel_sales.sum())
print("고객 유형 합계 일치:", total_sales == customer_sales.sum())

print("\n=== 4. 분석 문장 ===")
print(f"전체 주문 매출은 {total_sales:,}원입니다.")
print(f"카테고리 중 {top_category} 매출이 {category_sales.max():,}원으로 가장 높습니다.")
print(f"{top_channel} 매출은 {channel_sales.max():,}원으로 다른 채널보다 높습니다.")
print(f"{top_customer} 고객 매출은 {customer_sales.max():,}원으로 다른 고객 유형보다 높습니다.")
print(f"상품 중 {top_product} 매출이 {product_sales.max():,}원으로 가장 높습니다.")