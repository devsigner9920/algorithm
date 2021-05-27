from sys import stdin
from collections import Counter

s = Counter(stdin.readline().rstrip().upper()).most_common()
answer = s[0][0]
if len(s) > 1:
    if s[0][1] == s[1][1]:
        answer = '?'

print(answer)
