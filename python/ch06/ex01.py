weather = "맑음"
if weather == "비":
    print("우산을 챙기세요.") 


temp = int(input('오늘의 기온은 어때요'))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요")
elif 10 <= temp and temp < 30:
    print("활동하기 좋은 날씨에요.")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 외출을 자제하세요")