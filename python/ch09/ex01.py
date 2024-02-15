balance = 0 # 잔액

def open_account():
    print("새로운 계좌가 개설되었습니다.")
 
def deposit(money):
    global balance
    balance += money
    print(f'{money}원을 입금했습니다. 잔액은 {balance}입니다.')

def withdraw(money):
    global balance
    if balance > money:
        balance -= money
        print(f'{money}원을 출금합니다. 잔액은 {balance}입니다.')
        return True
    else:
        print('잔액이 부족합니다.')
        return False
    
open_account()
print(f'현재 잔액: {balance}')

deposit(5000)

r = withdraw(7000)
if r:
    print("^.^")
else:
    print("T.T")

r = withdraw(3000)
if r:
    print("^.^")
else:
    print("T.T")