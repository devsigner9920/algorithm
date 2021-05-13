import math

def solution(N, stages):
    answer = []
    stage_info = {i: (0, 0) for i in range(1, N + 1)}

    for i in range(1, N + 1):
        temp_p = 0
        temp_c = 0
        for stage in stages:
            if i == stage:
                temp_p += 1
            if i <= stage:
                temp_c += 1
        stage_info[i] = (temp_p, temp_c)

    for i in stage_info:
        (x, y) = stage_info[i]
        if y != 0:
            stage_info[i] = x / y
        else:
            stage_info[i] = 0

    answer = sorted(stage_info, key=lambda x: stage_info[x], reverse=True)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
