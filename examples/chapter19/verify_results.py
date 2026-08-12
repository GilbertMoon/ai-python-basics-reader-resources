# Chapter 19 - 예상 결과와 실제 결과 비교하기


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


expenses = [
    {"date": "2026-08-01", "category": "식비", "amount": 12000},
    {"date": "2026-08-02", "category": "교통", "amount": 3500},
    {"date": "2026-08-02", "category": "식비", "amount": 9000},
]

total = calculate_total(expenses)
category_totals = calculate_by_category(expenses)

print(total == 24500)
print(category_totals["식비"] == 21000)
print(category_totals["교통"] == 3500)
