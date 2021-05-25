from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    a, b = stdin.readline().rstrip().split()
    answer = [i_str * int(a) for i_str in list(b)]
    print(''.join(answer))