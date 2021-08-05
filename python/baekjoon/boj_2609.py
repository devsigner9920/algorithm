def gcd(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a


n, m = map(int, input().split())
gcd_num = gcd(n, m)

print(gcd_num)
print(int((n*m) / gcd_num))
