from sys import stdin

_ = stdin.readline().rstrip()
num = sum(int(i) for i in list(stdin.readline().rstrip()))

print(num)