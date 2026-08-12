# Chapter 11 - 리스트와 반복문

scores = [85, 55, 92, 48, 70]

for score in scores:
    if score >= 60:
        print(f"{score}점: 통과")
    else:
        print(f"{score}점: 재도전")
