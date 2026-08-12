# Chapter 19 - 종합 실습: 개인 지출 요약 프로그램


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


def show_report(total, category_totals):
    print("=== 지출 요약 ===")
    print(f"총 지출: {total:,}원")

    for category, amount in category_totals.items():
        print(f"{category}: {amount:,}원")


expenses = [
    {"date": "2026-08-01", "category": "식비", "amount": 12000},
    {"date": "2026-08-02", "category": "교통", "amount": 3500},
    {"date": "2026-08-02", "category": "식비", "amount": 9000},
]

total = calculate_total(expenses)
category_totals = calculate_by_category(expenses)
show_report(total, category_totals)
