# Chapter 23 - pandas로 지출 결과 다시 확인하기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter23" / "sample_expenses.csv"

df = pd.read_csv(file_path)

print("=== 데이터 ===")
print(df)

print("\n=== 전체 지출 ===")
print(df["amount"].sum())

print("\n=== 카테고리별 지출 ===")
print(df.groupby("category")["amount"].sum())
