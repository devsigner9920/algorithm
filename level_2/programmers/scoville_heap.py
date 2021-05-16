def solution(scoville, K):
    answer = 0
    del_arr = []

    for item in scoville:
        if item < K:
            del_arr.append(item)

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))