from sys import stdin

c = stdin.readline().rstrip()
a = c if len(c) == 2 else '0' + c
print(a)
cnt = 0
while True:
    b = int(a[0]) + int(a[1])
    a = str(a[1]) + str(b)[-1]
    cnt += 1
    if int(a) == int(c):
        break
print(cnt)
