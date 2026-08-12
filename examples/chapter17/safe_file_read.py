# Chapter 17 - FileNotFoundError 처리하기

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "chapter17" / "message.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    print("파일 이름과 경로를 확인해 주세요.")
else:
    print(content)
