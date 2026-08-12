# Chapter 13 - 딕셔너리 추가, 수정, 삭제

product = {
    "name": "무선 마우스",
    "price": 25000,
    "stock": 12
}

product["category"] = "주변기기"
product["price"] = 23000
removed_stock = product.pop("stock")

print(product)
print("삭제된 재고:", removed_stock)
