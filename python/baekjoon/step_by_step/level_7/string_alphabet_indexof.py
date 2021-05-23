from sys import stdin

answer = []
in_str = stdin.readline().rstrip()
for i in range(ord('a'), ord('z') + 1):
    try:
        answer.append(str(in_str.index(chr(i))))
    except ValueError:
        answer.append('-1')

print(' '.join(answer))