from sys import stdin

s = [int(stdin.readline().rstrip()) for _ in range(9)]
s_sum = sum(s)

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if 100 == s_sum - (s[i] + s[j]):
            n1, n2 = s[i], s[j]
            s.remove(n1)
            s.remove(n2)
            s.sort()

            for l in range(len(s)): print(s[l])
            break

    if len(s) == 7: break

