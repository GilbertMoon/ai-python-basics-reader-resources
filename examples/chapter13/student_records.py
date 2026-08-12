# Chapter 13 - 딕셔너리의 리스트로 학생 성적 관리

students = [
    {"name": "민수", "score": 85},
    {"name": "지영", "score": 92},
    {"name": "서준", "score": 78}
]

total = 0

for student in students:
    print(f"{student['name']}: {student['score']}점")
    total += student["score"]

average = total / len(students)
print(f"평균: {average:.1f}점")
