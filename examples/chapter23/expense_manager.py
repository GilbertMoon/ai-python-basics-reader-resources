# Chapter 23 - 종합 프로젝트: 개인 지출 관리 프로그램

import csv
from pathlib import Path


FILE_PATH = Path(__file__).with_name("expenses.csv")
FIELDNAMES = ["date", "category", "description", "amount"]


def load_expenses(file_path):
    expenses = []

    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["amount"] = int(row["amount"])
                except ValueError:
                    print("금액이 올바르지 않은 행은 건너뜁니다:", row)
                    continue

                expenses.append(row)
    except FileNotFoundError:
        return []

    return expenses


def save_expenses(file_path, expenses):
    with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    date = input("날짜(YYYY-MM-DD): ").strip()
    category = input("카테고리: ").strip()
    description = input("내용: ").strip()

    if not date or not category or not description:
        print("날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
        return

    try:
        amount = int(input("금액: "))
    except ValueError:
        print("금액은 정수로 입력해 주세요.")
        return

    if amount <= 0:
        print("금액은 0보다 큰 값으로 입력해 주세요.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    }

    expenses.append(expense)
    print("지출 내역을 추가했습니다.")


def show_expenses(expenses):
    if not expenses:
        print("등록된 지출이 없습니다.")
        return

    print("\n=== 지출 내역 ===")
    number = 1

    for expense in expenses:
        print(
            f"{number}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']:,}원"
        )
        number += 1


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
    if not expenses:
        print("요약할 지출이 없습니다.")
        return

    total = calculate_total(expenses)
    category_totals = calculate_by_category(expenses)

    print("\n=== 지출 요약 ===")
    print(f"전체 지출: {total:,}원")
    print("카테고리별 지출:")

    for category, amount in category_totals.items():
        print(f"- {category}: {amount:,}원")


def main():
    expenses = load_expenses(FILE_PATH)
    print(f"기존 지출 {len(expenses)}건을 불러왔습니다.")

    while True:
        print("\n=== 개인 지출 관리 ===")
        print("1. 지출 추가")
        print("2. 지출 목록")
        print("3. 지출 요약")
        print("4. 저장")
        print("0. 종료")

        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            save_expenses(FILE_PATH, expenses)
            print("CSV 파일에 저장했습니다.")
        elif choice == "0":
            save_expenses(FILE_PATH, expenses)
            print("저장 후 프로그램을 종료합니다.")
            break
        else:
            print("메뉴 번호를 다시 확인해 주세요.")


main()