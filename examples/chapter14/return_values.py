# Chapter 14 - 반환값 사용하기

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference


sum_value, diff_value = calculate(10, 3)

print("합:", sum_value)
print("차:", diff_value)
