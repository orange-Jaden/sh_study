# 1 ~ 20000 사이 4의 배수를 제외한 모든 수 더하기
sum :int = 0
i :int = 0

while True:
    i += 1
    if i >= 20000:
        break
    elif i % 4 == 0: 
        continue

    print(f'{i}를 sum에 더합니다.')
    sum += i
    i += 1

print(f'sum의 값은 \'{sum}\' 입니다.')
