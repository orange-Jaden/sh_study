inputStr = "1 3 5"
print(inputStr)

strList = inputStr.split()
print(strList)

for e in strList:
    int(e) + 1

print(map(int, strList))
print(list(map(int, strList)))

for i in map(int, strList):
    print(i + 1)


l = list(map(int, input().split()))