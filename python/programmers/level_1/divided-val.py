def solution(arr, divisor):
    answer = []

    for item in sorted(arr):
        if item % divisor == 0:
            answer.append(item)

    return answer if len(answer) > 0 else [-1]


print(solution([15, 5, 9, 7, 10], 5))
