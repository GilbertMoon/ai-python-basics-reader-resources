# Chapter 20 - 논리 오류 찾기 실습
# 조건 순서가 잘못되어 높은 점수도 D로 분류될 수 있습니다.


def get_grade(score):
    if score >= 60:
        return "D"
    elif score >= 70:
        return "C"
    elif score >= 80:
        return "B"
    elif score >= 90:
        return "A"
    return "F"


test_scores = [59, 60, 69, 70, 79, 80, 89, 90, 100]

for score in test_scores:
    print(score, get_grade(score))
