# Chapter 20 - 디버깅 실습용 코드
# 아래 코드는 50,000원 경계값에서 의도적으로 잘못된 결과가 나옵니다.


def calculate_shipping(order_amount):
    if order_amount > 50000:
        return 0
    return 3000


print("40,000원 주문:", calculate_shipping(40000))
print("50,000원 주문:", calculate_shipping(50000))
print("60,000원 주문:", calculate_shipping(60000))
