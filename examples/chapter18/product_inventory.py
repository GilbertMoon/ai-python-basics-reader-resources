# Chapter 18 - 종합 실습: 상품 재고 객체


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def restock(self, quantity):
        self.stock += quantity

    def show_info(self):
        print(f"{self.name} / {self.price:,}원 / 재고 {self.stock}개")


products = [
    Product("키보드", 45000, 10),
    Product("마우스", 25000, 5),
    Product("웹캠", 65000, 3),
]

products[0].show_info()

if products[0].sell(3):
    print("판매 처리 완료")
else:
    print("재고가 부족합니다.")

products[0].restock(2)
products[0].show_info()
