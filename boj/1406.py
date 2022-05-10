# https://www.acmicpc.net/problem/1406
"""
에디터
"""
import sys

left = list(sys.stdin.readline().strip())
right = []
m = int(sys.stdin.readline())

for _ in range(m):
    command = sys.stdin.readline().strip()

    if command[0] == 'L' and left:
        right.append(left.pop())
        continue

    if command[0] == 'B' and left:
        left.pop()
        continue

    if command[0] == 'D' and right:
        left.append(right.pop())
        continue

    if command[0] == 'P':
        left.append(command[2])

right.reverse()
print(''.join(left + right))