# Chapter 17 - 예외 처리를 적용한 간단 계산기


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    return None


try:
    first = float(input("첫 번째 숫자: "))
    operator = input("연산자(+ - * /): ").strip()
    second = float(input("두 번째 숫자: "))

    result = calculate(first, second, operator)
except ValueError:
    print("숫자 형식을 확인해 주세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    if result is None:
        print("지원하지 않는 연산자입니다.")
    else:
        print(f"결과: {result}")
