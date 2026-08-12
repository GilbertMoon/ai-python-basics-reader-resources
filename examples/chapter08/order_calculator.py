customer = input("고객 이름: ").strip()
product = input("상품명: ").strip()
price = int(input("상품 가격: "))
quantity = int(input("수량: "))

total = price * quantity

print("-" * 30)
print(f"고객: {customer}")
print(f"상품: {product}")
print(f"가격: {price}원")
print(f"수량: {quantity}개")
print(f"총 금액: {total}원")
