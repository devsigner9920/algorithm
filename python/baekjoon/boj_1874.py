import sys

input = sys.stdin.readline

n = int(input())
targets = [int(input()) for _ in range(n)]

flag = True
stack, answer, current = [], [], 0

for target in targets:
    while True:
        if stack and stack[-1] == target:
            answer.append('-')
            stack.pop()
            break

        elif current > target:
            flag = False

        else:
            current += 1
            stack.append(current)
            answer.append('+')

        if not flag:
            print('NO')
            exit()

if flag:
    print('\n'.join(answer))