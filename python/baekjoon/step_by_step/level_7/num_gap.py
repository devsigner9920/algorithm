from sys import stdin

x, y = map(list, stdin.readline().rstrip().split())
a, b = int(''.join(reversed(x))), int(''.join(reversed(y)))
print(a if a > b else b)