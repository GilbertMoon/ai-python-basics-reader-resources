# Chapter 09 - 종합 실습: 배송비 안내

order_amount = int(input("주문 금액을 입력하세요: "))

if order_amount >= 50000:
    shipping_fee = 0
else:
    shipping_fee = 3000

final_amount = order_amount + shipping_fee

print(f"주문 금액: {order_amount}원")
print(f"배송비: {shipping_fee}원")
print(f"최종 결제 금액: {final_amount}원")
