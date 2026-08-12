# Chapter 18 - __init__과 속성


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


product = Product("키보드", 45000, 10)

print(product.name)
print(product.price)
print(product.stock)

product.price = 42000
product.stock = 8

print(product.price)
print(product.stock)
