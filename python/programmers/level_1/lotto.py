def solution(lottos, win_nums):
    answer = []
    ok = 0
    blank = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            blank += 1
            continue
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                ok += 1
                win_nums.pop(j)
                break

    max_rank = len(lottos) - (ok + blank) + 1 if ok + blank != 0 else len(lottos)
    min_rank = len(lottos) - ok + 1 if ok != 0 else len(lottos)
    answer.append(max_rank)
    answer.append(min_rank)
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
