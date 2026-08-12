# Chapter 17 - ValueError 처리하기

try:
    age = int(input("나이를 입력하세요: "))
    print(f"입력한 나이: {age}")
except ValueError:
    print("나이는 정수로 입력해 주세요.")
