# 사용자 메뉴
choice = 1

# 잔액
balance = 0

# 거래내역
history = []

while True:

    print(
        """
        1. 잔액조회
        2. 입금
        3. 출금
        4. 거래내역 조회
        0. 종료
        """
    )

    choice = input("입력: ")  # 1, 2
    choice = int(choice)

    # 종료
    if choice == 0:
        break

    # 잔액조회
    elif choice == 1:
        print(f"1. 현재잔액 : {balance}")

    # 입금
    elif choice == 2:
        amount = input("2. 입금 금액 입력 : ")
        amount = int(amount)
        if amount <= 0:
            print("오류 - 올바른 금액을 입력하세요.")
            continue
        balance += amount

        # 거래내역 쌓기
        data = {
            "type": "입금",
            "amount": amount,
            "balance": balance,
        }
        history.append(data)

    # 출금
    elif choice == 3:
        amount = input("3. 출금액 입력 : ")
        amount = int(amount)
        if amount <= 0:
            print("오류")
            continue
        elif amount > balance:
            print("잔액부족")
            continue
        balance -= amount
        # 거래내역 쌓기
        data = {
            "type": "출금",
            "amount": amount,
            "balance": balance,
        }
        history.append(data)
    # 거래내역 조회
    elif choice == 4:
        for h in history:
            print(f"[{h["type"]}] {h["amount"]} {h["balance"]}")
