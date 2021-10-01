n, k = map(int, input().split())
a = list()

for _ in range(n):
    a.append(int(input()))

result = 0

def coin_zero():
    global k, a, result
    for i in range(n-1, -1, -1):
        quot = k // a[i]
        remaind = k % a[i]
        if quot > 0:
            result += quot
            k = remaind
    return result

print(coin_zero())