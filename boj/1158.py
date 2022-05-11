# https://www.acmicpc.net/problem/1158
"""
요세푸스 문제
"""
import sys
import collections

n, k = map(int, sys.stdin.readline().rstrip().split())

que = collections.deque([i for i in range(1, n + 1)])
results = []

i = 1
while que:
    e = que.popleft()
    if i == k:
        results.append(e)
        i = 1
        continue

    que.append(e)
    i += 1

print(f'<{", ".join(map(str, results))}>')