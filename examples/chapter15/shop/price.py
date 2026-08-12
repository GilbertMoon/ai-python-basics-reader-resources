# Chapter 15 - 패키지 안의 가격 계산 모듈


def calculate_total(price, quantity):
    return price * quantity


def apply_discount(total, rate=0.1):
    return total * (1 - rate)
