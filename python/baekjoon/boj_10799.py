t = list(input())
sticks = []
result = 0
for i in range(len(t)):
    if t[i] == '(':
        if t[i + 1] == '(':
            sticks.append(t[i])
        elif t[i + 1] == ')':
            t[i] = '0'
            t[i + 1] = '0'
            result += len(sticks)
    elif t[i] == ')':
        sticks.pop()
        result += 1

print(result)