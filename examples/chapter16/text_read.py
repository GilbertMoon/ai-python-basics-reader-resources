# Chapter 16 - 텍스트 파일 읽기

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter16" / "memo.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
