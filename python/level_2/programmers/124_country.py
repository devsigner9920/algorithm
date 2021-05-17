RULE = '412'

def solution(n):
    r = n % 3
    q = n // 3 if r != 0 else (n // 3) - 1

    return solution(q) + RULE[r] if q else RULE[r]

print(solution(21))
