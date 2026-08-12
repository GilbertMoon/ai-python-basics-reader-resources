# Chapter 18 - 여러 객체 만들고 리스트로 관리하기


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}: {self.price:,}원")


products = [
    Product("키보드", 45000),
    Product("마우스", 25000),
    Product("웹캠", 65000),
]

for product in products:
    product.show_info()

price_total = 0
for product in products:
    price_total += product.price

print(f"가격 합계: {price_total:,}원")
