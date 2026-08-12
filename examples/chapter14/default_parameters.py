# Chapter 14 - 기본값 매개변수와 키워드 인수

def greet(name, message="안녕하세요", city="서울"):
    print(f"{message}, {name}님!")
    print(f"도시: {city}")


greet("민수")
print()
greet("지영", "반갑습니다", "부산")
print()
greet(city="대전", name="서준")
