# Chapter 20 - 동작을 유지하면서 중복 줄이기


def calculate_shipping(order_amount):
    if order_amount >= 50000:
        return 0
    return 3000


def show_order_report(name, order_amount):
    shipping = calculate_shipping(order_amount)
    final_amount = order_amount + shipping

    print(f"주문자: {name}")
    print(f"상품 금액: {order_amount:,}원")
    print(f"배송비: {shipping:,}원")
    print(f"최종 결제 금액: {final_amount:,}원")


show_order_report("민수", 42000)
print()
show_order_report("지영", 72000)
