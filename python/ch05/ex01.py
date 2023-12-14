subway1 = 10
subway2 = 20
subway3 = 30
print(subway1)
print(subway2)
print(subway3)

# 리스트 생성
subway =  [10, 20, 30]
for p in subway:
    print(p)

# 리스트 값 추가/삽입/삭제
subway=["푸","피글렛","티거"]
print(subway.index("피글렛"))
subway.append("이요르")
print(subway)
subway.insert(1,"루")
print(subway)

lastitem = subway.pop()
print(lastitem)
print(subway)
del subway[1]
print(subway)
print(subway.pop(1))
print(subway)
subway.clear()
print(subway)


subway=["푸","피글렛","티거", "이요르"]
print(subway[0]) # 푸
print(subway[1]) # 피글렛
print(subway[2]) # 티거
print(subway[3]) # 이요르

print(subway[1:])   # ["피글렛","티거", "이요르"]
print(subway[:2])   # ["푸","피글렛"]
print(subway[1:3])  # ["피글렛","티거"]
print(subway[1:2])  # ["피글렛"]

# 중복 값 확인하기
subway=["푸","피글렛","티거", "이요르", "푸"]
print(subway.count("푸")) 

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

num_list = [5,2,4,3,1]
num_list.sort(reverse=True)
print(num_list)

# sorted() 함수 사용하기
origin_list = [5,2,4,3,1]
new_list = sorted(origin_list)
print('origin list:', origin_list)
print('new list:', new_list)

# 리스트 합치기
## 리스트 포함시키기
list1 = ["푸", 20, True]
list2 = ["피글렛", 30, False]
list1.append(list2)
print(list1)

## 리스트 확장하기 
list1 = ["푸", 20, True]
list2 = ["피글렛", 30, False]
print(list1 + list2)
list1.extend(list2)
print(list1)
print()