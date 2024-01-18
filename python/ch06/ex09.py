import random

grades = ['조금 더 노력해주세요', '잘하셨습니다.', '만점입니다. 축하합니다.']
# list which have 100 random elements
scores = [random.randint(0, 100) for _ in range(26)]

print(scores)

for score in scores:
    print(f'점수는 {score}입니다. {grades[score//50]}')