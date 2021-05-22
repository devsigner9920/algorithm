from sys import stdin

t = int(stdin.readline().rstrip())

for i in range(t):
    a, b = map(int, stdin.readline().rstrip().split())
    print(a + b)
