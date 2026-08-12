# Chapter 09 - 논리 연산자와 조건문

age = 25
day = "토요일"
is_closed = False

if 20 <= age < 30:
    print("20대입니다.")

if day == "토요일" or day == "일요일":
    print("주말입니다.")

if not is_closed:
    print("현재 이용할 수 있습니다.")
