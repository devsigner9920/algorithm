from sys import stdin

t = int(stdin.readline().rstrip())

for i in range(1, t + 1):
    print(' ' * (t - i) + '*' * i)