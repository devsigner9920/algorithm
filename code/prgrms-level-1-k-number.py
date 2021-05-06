def solution(array, commands):
    answer = []

    # my solution
    for com in commands:
        arr = array[com[0] - 1:com[1]]
        arr.sort()
        answer.append(arr[com[2] - 1])

    # better solution
    # for i, j, k in commands:
    #     answer.append(list(sorted(array[i - 1:j]))[k - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

