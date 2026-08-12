# Chapter 21 - Series와 DataFrame 기초

import pandas as pd


df = pd.DataFrame({
    "name": ["민수", "지영", "서준"],
    "score": [85, 92, 78],
})

print(df)
print()
print(df["score"])
print(type(df))
print(type(df["score"]))
