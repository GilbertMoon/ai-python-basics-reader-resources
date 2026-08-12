# Chapter 14 - 학생 점수 보고서

def calculate_average(scores):
    return sum(scores) / len(scores)


def get_result(average):
    if average >= 60:
        return "통과"
    return "재도전"


def show_report(name, scores):
    average = calculate_average(scores)
    result = get_result(average)

    print(f"학생: {name}")
    print(f"점수: {scores}")
    print(f"평균: {average:.1f}")
    print(f"결과: {result}")


show_report("민수", [80, 75, 90])
