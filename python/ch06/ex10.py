fruits = {
    "apple": "사과",
    "banana": "바나나",
    "orange": "오렌지",
    "grape": "포도",
    "strawberry": "딸기",
    "watermelon": "수박",
    "pineapple": "파인애플",
    "mango": "망고",
    "peach": "복숭아"
}

print(fruits['apple'])

for en, kr in fruits.items():
    print(f'{en}: {kr}')

for en in fruits.keys():
    print(en)

for kr in fruits.values():
    print(kr)