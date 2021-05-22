a = int(input())
b = str(input())

result = 0
for i in range(len(b)):
    #print(a * int(b[i]))
    sol = a * int(b[2 - i])
    print(sol)
    result += sol * (10 ** i)
print(result)