my_password :str = "password"
password :str = ""

i = 0
while password != my_password:
    password :str = input('password를 입력해주세요> ')
    i += 1
    if i >= 5:
        print("비밀번호 입력 횟수 초과입니다.")
        exit()

print('로그인 되었습니다.')