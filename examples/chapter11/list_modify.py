# Chapter 11 - 리스트 추가, 수정, 삭제

todos = ["파이썬 복습", "책 읽기"]
print("처음:", todos)

todos.append("산책하기")
todos.insert(1, "강의 듣기")
print("추가 후:", todos)

todos[0] = "파이썬 예제 복습"
print("수정 후:", todos)

todos.remove("책 읽기")
print("삭제 후:", todos)
