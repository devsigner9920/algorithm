from sys import stdin

x = 1
for _ in range(3):
    x = x * int(stdin.readline().rstrip())

list_x = list(str(x))

for i in range(10):
    print(list_x.count(str(i)))