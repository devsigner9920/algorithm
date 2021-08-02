import sys

n = list(sys.stdin.readline().rstrip())

opers = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

post = []
op_stack = []
for i in n:
    if i.isalpha():
        post.append(i)
    elif i == '(':
        op_stack.append(i)
    elif i == ')':
        while op_stack and op_stack[-1] != '(':
            post.append(op_stack.pop())
        op_stack.pop()
    else:
        while op_stack and opers[i] <= opers[op_stack[-1]]:
            post.append(op_stack.pop())
        op_stack.append(i)

while len(op_stack) != 0:
    post.append(op_stack.pop())

print(''.join(post))
