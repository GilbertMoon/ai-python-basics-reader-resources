# Chapter 24 - 주문 데이터 구조 점검하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter24" / "orders.csv"

df = pd.read_csv(file_path)

print("=== 데이터 크기 ===")
print(df.shape)

print("\n=== 열 이름 ===")
print(list(df.columns))

print("\n=== 자료형 ===")
print(df.dtypes)

print("\n=== 결측값 ===")
print(df.isna().sum())

print("\n=== 앞쪽 5행 ===")
print(df.head())
