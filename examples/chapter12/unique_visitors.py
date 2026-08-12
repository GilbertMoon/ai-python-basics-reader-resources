# Chapter 12 - 고유 방문자 분석

monday_list = ["민수", "지영", "민수", "서준", "하나"]
tuesday_list = ["지영", "유진", "서준", "유진"]

monday = set(monday_list)
tuesday = set(tuesday_list)

both_days = monday & tuesday
monday_only = monday - tuesday
all_visitors = monday | tuesday

print("월요일 고유 방문자:", monday)
print("화요일 고유 방문자:", tuesday)
print("이틀 모두 방문:", both_days)
print("월요일만 방문:", monday_only)
print("전체 고유 방문자 수:", len(all_visitors))
