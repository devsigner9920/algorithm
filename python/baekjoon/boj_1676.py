from math import factorial

n = int(input())
count = 0
fac = list(str(factorial(n)))


while True:
    if fac.pop() == '0':
        count += 1
    else:
        break

print(count)