def d(n):
    a = n
    if a < len(arr):
        arr[a] = False
        a = a + sum(list(map(int, str(a))))
        return d(a)


arr = [True] * 10000
for i in range(len(arr)):
    d(i + 1)


