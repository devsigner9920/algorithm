from sys import stdin

x = [0]
for i in range(9):
    num = int(stdin.readline().rstrip())
    if x[0] < num:
        x.clear()
        x.append(num)
        x.append(i + 1)

for i in x:
    print(i)
