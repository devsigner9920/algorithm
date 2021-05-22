from sys import stdin

t = int(stdin.readline().rstrip())
x = list(map(int, stdin.readline().rstrip().split()))
max_num = max(x)
print(sum([i / max_num * 100 for i in x]) / t)

