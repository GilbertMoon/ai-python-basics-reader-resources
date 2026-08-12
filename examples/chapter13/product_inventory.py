# Chapter 13 - 상품 재고 관리

products = [
    {"name": "키보드", "price": 45000, "stock": 8},
    {"name": "마우스", "price": 25000, "stock": 4},
    {"name": "웹캠", "price": 65000, "stock": 3}
]

total_stock = 0

for product in products:
    print(f"{product['name']}: {product['price']}원")
    total_stock += product["stock"]

    if product["stock"] <= 5:
        print(f"  재고 부족: {product['stock']}개")

products[0]["price"] = 42000

print(f"전체 재고: {total_stock}개")
print(f"수정된 키보드 가격: {products[0]['price']}원")
