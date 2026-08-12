# Chapter 23 - 전체 지출과 카테고리별 합계 출력하기


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


def show_summary(expenses):
    total = calculate_total(expenses)
    category_totals = calculate_by_category(expenses)

    print(f"전체 지출: {total:,}원")
    print("=== 카테고리별 지출 ===")

    for category, amount in category_totals.items():
        print(f"{category}: {amount:,}원")


expenses = [
    {"date": "2026-08-01", "category": "식비", "description": "점심", "amount": 12000},
    {"date": "2026-08-01", "category": "교통", "description": "버스", "amount": 1500},
    {"date": "2026-08-02", "category": "카페", "description": "커피", "amount": 4800},
    {"date": "2026-08-02", "category": "식비", "description": "저녁", "amount": 15000},
]

show_summary(expenses)
