# Chapter 19 - 카테고리별 합계 계산하기


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

print(calculate_by_category(expenses))
