# Chapter 17 - 여러 예외 구분해서 처리하기

try:
    number = int(input("100을 나눌 정수를 입력하세요: "))
    result = 100 / number
    print(f"결과: {result}")
except ValueError:
    print("정수를 입력해 주세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
