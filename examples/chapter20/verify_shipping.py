# Chapter 20 - 경계값으로 버그 찾기
# 의도적으로 잘못된 함수가 어떤 입력에서 실패하는지 확인합니다.


def calculate_shipping(order_amount):
    if order_amount > 50000:
        return 0
    return 3000


print(calculate_shipping(49999) == 3000)
print(calculate_shipping(50000) == 0)
print(calculate_shipping(50001) == 0)
