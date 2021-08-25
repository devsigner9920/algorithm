# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    a = sorted(filter(lambda x: x > 0, set(A)))
    if len(a) == 0:
        return 1
    else:
        sol = 1
        for i in range(len(a)):
            if a[i] == sol:
                sol += 1
            else:
                return sol
    return sol


print(solution([1, 3, 6, 4, 1, 2]))
solution([-1, -3])
