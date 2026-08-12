# Chapter 12 - 집합 연산

team_a = {"Python", "SQL", "AI"}
team_b = {"Python", "Java", "AI"}

all_skills = team_a | team_b
common_skills = team_a & team_b
only_a = team_a - team_b

print("전체 기술:", all_skills)
print("공통 기술:", common_skills)
print("A팀만:", only_a)
