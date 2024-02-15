balance = 0

def open_account():
    global balance
    balance = 0
    print("계좌가 개설되었습니다.")

def deposit(balance, money):
    print(f"{money}원을 입금합니다.")
    balance = balance + money

    return balance


def withdraw(balance, money):
    print("출금")

    if balance >= money:
        print("출금합니다.")
        balance = balance - money
        return balance 
    else:
        print("출금 실패")
        return balance

def printBalance(balance):
    print(f'현재 잔액: {balance}입니다.')    

open_account()
printBalance(balance)

balance = deposit(balance, 6000)
printBalance(balance)

balance = withdraw(balance, 3000)
printBalance(balance)