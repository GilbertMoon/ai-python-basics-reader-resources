# Chapter 20 - 최소 수정 후 다시 검증하기


def calculate_shipping(order_amount):
    if order_amount >= 50000:
        return 0
    return 3000


tests = [
    (40000, 3000),
    (49999, 3000),
    (50000, 0),
    (50001, 0),
    (60000, 0),
]

for order_amount, expected in tests:
    actual = calculate_shipping(order_amount)
    print(order_amount, actual == expected)
