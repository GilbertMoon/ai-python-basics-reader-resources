# Chapter 15 - 패키지의 모듈 사용하기

from shop.price import calculate_total, apply_discount

subtotal = calculate_total(12000, 3)
final_price = apply_discount(subtotal)

print(subtotal)
print(final_price)
