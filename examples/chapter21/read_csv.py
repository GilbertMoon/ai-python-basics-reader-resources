# Chapter 21 - CSV 파일을 DataFrame으로 읽기

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter21" / "store_sales.csv"

df = pd.read_csv(file_path)

print(df)
