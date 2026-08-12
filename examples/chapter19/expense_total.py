# Chapter 19 - 가장 작은 기능부터 구현하기


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


expenses = [
    {"date": "2026-08-01", "category": "식비", "amount": 12000},
    {"date": "2026-08-02", "category": "교통", "amount": 3500},
    {"date": "2026-08-02", "category": "식비", "amount": 9000},
]

print(calculate_total(expenses))
