# Chapter 11 - 종합 실습: 장보기 목록

shopping = ["우유", "달걀", "사과"]

print("처음 목록:", shopping)

shopping.append("빵")
shopping.remove("달걀")
shopping.sort()

print("수정된 목록:")
for item in shopping:
    print(f"- {item}")

print(f"총 {len(shopping)}개를 구매해야 합니다.")
