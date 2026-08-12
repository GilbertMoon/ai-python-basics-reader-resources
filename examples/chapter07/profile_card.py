name = "  문길동  "
city = "seoul"
language = "Python"

clean_name = name.strip()
city_upper = city.upper()

print(f"이름: {clean_name}")
print(f"도시: {city_upper}")
print(f"학습 언어: {language}")
print(f"{clean_name}님은 {language}을 공부하고 있습니다.")
print(f"학습 언어 글자 수: {len(language)}")
print(f"첫 글자: {language[0]}")
print(f"마지막 글자: {language[-1]}")
