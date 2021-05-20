from sys import stdin

t = int(stdin.readline().rstrip())
for _ in range(t):
    ox = stdin.readline().rstrip()
    a = 1
    answer = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            answer += a
            a += 1
        else:
            a = 1
    print(answer)