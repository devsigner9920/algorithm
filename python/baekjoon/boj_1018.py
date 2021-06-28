from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
chess = [stdin.readline().rstrip() for _ in range(n)]

test = ''
for i in range(n - 7):
    for j in range(m - 7):
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                test += chess[k][l]
            test += '\n'
        test += '==========================\n'

print(test)