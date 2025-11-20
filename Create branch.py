import datetime

def d_day():
    print("=== D-Day 계산기 ===")
    target = input("목표 날짜(YYYY-MM-DD) 입력: ")
    year, month, day = map(int, target.split("-"))
    target_date = datetime.date(year, month, day)

    today = datetime.date.today()
    diff = target_date - today
    print(f"{target_date} 까지 {diff.days}일 남았습니다.\n")

def date_diff():
    print("=== 두 날짜 차이 계산 ===")
    d1 = input("첫 번째 날짜(YYYY-MM-DD): ")
    d2 = input("두 번째 날짜(YYYY-MM-DD): ")

    y1, m1, d1 = map(int, d1.split("-"))
    y2, m2, d2 = map(int, d2.split("-"))

    date1 = datetime.date(y1, m1, d1)
    date2 = datetime.date(y2, m2, d2)

    diff = abs(date2 - date1)
    print(f"{date1} 와 {date2} 의 차이는 {diff.days}일입니다.\n")

while True:
    print("=== 날짜 계산기 ===")
    print("1) D-Day 계산")
    print("2) 두 날짜 사이 계산")
    print("0) 종료")

    choice = input("선택: ")

    if choice == "1":
        d_day()
    elif choice == "2":
        date_diff()
    elif choice == "0":
        print("프로그램 종료!")
        break
    else:
        print("잘못 입력했습니다.\n")
