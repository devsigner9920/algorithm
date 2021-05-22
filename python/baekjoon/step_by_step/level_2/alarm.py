h, m = map(int, input().split())

a = h
b = m - 45
if b < 0:
    b = 60 + b
    a -= 1

if a < 0:
    a = 23

print('%d %d' % (a, b))