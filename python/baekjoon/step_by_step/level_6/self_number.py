def d(n):
    divided_num = sum(map(int, list(str(n))))
    exist_num = n + divided_num
    return exist_num

isSelfNum = [True] * 10000

for i in range(len(isSelfNum)):
    checkNum = d(i + 1)
    if checkNum <= 10000:
        isSelfNum[checkNum - 1] = False

i = 1
for item in isSelfNum:
    if item:
        print(i)
    i += 1