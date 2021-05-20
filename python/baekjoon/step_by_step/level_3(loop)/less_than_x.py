from sys import stdin

n, x = map(int, stdin.readline().rstrip().split())

a = stdin.readline().rstrip().split()
b = []

for i in range(n):
    if int(a[i]) < x:
        b.append(a[i])

print(' '.join(b))
