from sys import stdin

def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


t = int(stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, stdin.readline().rstrip().split())
    print(int((n * m) / gcd(n, m)))
