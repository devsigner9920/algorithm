def solution(arr):
    answer = []

    for item in arr:
        if len(answer) == 0 or answer[-1] != item:
            answer.append(item)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
