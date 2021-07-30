n = int(input())

for i in range(0, n):
    t = i + sum(map(int, list(str(i))))
    if t == n:
        print(i)
        break
    if i == n - 1:
        print(0)
