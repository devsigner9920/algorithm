n = int(input())
after = ' '.join(list(input()))
stack = []

for i in range(n):
    after = after.replace(chr(65 + i), input())
after = after.split()
for a in after:
    if a.isalnum():
        stack.append(int(a))
    else:
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        if a == '+':
            stack.append(tmp1 + tmp2)
        elif a == '-':
            stack.append(tmp2 - tmp1)
        elif a == '*':
            stack.append(tmp1 * tmp2)
        elif a == '/':
            stack.append(tmp2 / tmp1)

print('%.2f' % stack[0])