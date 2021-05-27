from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())

margin = c - b

if margin <= 0:
    print(-1)
else:
    print(a // margin + 1)