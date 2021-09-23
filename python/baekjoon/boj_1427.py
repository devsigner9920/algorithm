import sys

N = list(map(str,sys.stdin.readline()))

result = []

for i in N:
    result.append(i)

result.sort()
result.reverse()

print(''.join(result))