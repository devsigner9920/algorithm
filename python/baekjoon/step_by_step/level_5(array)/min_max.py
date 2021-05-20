from sys import stdin

n = int(stdin.readline().rstrip())
x = stdin.readline().rstrip().split()

print(min(int(i) for i in x), max(int(i) for i in x))