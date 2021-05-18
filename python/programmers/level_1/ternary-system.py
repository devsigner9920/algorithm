def ternary(number):
    q, r = divmod(number, 3)
    n = str(r)
    return ternary(q) + n if q else n


def solution(n):
    answer = 0
    tern = ternary(n)
    arr = list(tern)

    for i in range(len(arr)):
        answer += 3 ** i * int(arr[i])

    return answer


solution(125)
