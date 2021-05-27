from sys import stdin

dial = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9 : 'WXYZ'}

a = 'STR'
answer = 0
for x in stdin.readline().rstrip():
    for k, v in dial.items():
        if v.find(x) > -1:
            answer += k + 1

print(answer)