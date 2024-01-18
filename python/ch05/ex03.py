menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])

item_1, item_2 = menu
print(item_1)
print(item_2)

name, age, hobby = ("피글렛", 20, "코딩")   # 소괄호 생략 가능
print(hobby)

# 스왑
departure, arrival = "대구", "제주"
departure, arrival = arrival, departure

print(f'departure: {departure}, arrival: {arrival}')