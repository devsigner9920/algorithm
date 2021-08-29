import sys


def solution(A, K):
    answer = sys.maxsize
    for i in range(len(A)):
        if (len(A) - i) < K:
            break
        result = A[:i] + A[i + K:]
        tmp = max(result) - min(result)
        if answer > tmp: answer = tmp
    return answer


print(solution([5, 3, 6, 1, 3], 2))

