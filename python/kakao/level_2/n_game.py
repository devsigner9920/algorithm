import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    s = ''
    i = 0
    while len(s) < t*m:
        s += convert(i, n)
        i += 1
    routine = 0
    if p == 1: routine = 1 + p
    else: routine = p
    for i in range(p - 1, len(s), routine):
        answer += s[i]
        if len(answer) == t: break
    return answer


print(solution(2, 4, 2, 1))