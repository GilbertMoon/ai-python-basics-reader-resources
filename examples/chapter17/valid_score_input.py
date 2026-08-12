# Chapter 17 - 올바른 점수를 입력할 때까지 반복하기

while True:
    try:
        score = int(input("점수(0~100): "))
    except ValueError:
        print("숫자로 입력해 주세요.")
        continue

    if 0 <= score <= 100:
        break

    print("0부터 100 사이의 값을 입력해 주세요.")

print(f"입력된 점수: {score}")
