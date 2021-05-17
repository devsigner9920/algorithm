def solution(n, lost, reserve):
    answer = n - len(lost)

    intersection = set(lost) & set(reserve)
    lost = list(set(lost) - intersection)
    reserve = list(set(reserve) - intersection)
    answer += len(intersection)
    while len(lost) != 0:
        item = lost.pop(0)
        if reserve.count(item - 1) > 0:
            reserve.remove(item - 1)
            answer += 1
            continue
        if reserve.count(item + 1) > 0:
            reserve.remove(item + 1)
            answer += 1
            continue
    return answer


print(solution(5,[1, 2, 3],[2, 3, 4]))

