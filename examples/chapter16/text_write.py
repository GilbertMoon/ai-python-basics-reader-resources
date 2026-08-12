# Chapter 16 - 텍스트 파일 쓰기와 추가하기

from pathlib import Path

output_path = Path(__file__).with_name("study_log.txt")

with open(output_path, "w", encoding="utf-8") as file:
    file.write("파이썬 파일 쓰기 실습\n")
    file.write("오늘은 with open()을 배웠습니다.\n")

with open(output_path, "a", encoding="utf-8") as file:
    file.write("CSV 파일도 이어서 공부합니다.\n")

print("저장 위치:", output_path)
