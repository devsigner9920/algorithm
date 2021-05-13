def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    solArr = []

    for ln in lost:
        if reserve.count(ln - 1) == 1 and solArr.count(ln - 1) == 0:
            solArr.append(ln - 1)
            continue
        elif reserve.count(ln + 1) == 1 and solArr.count(ln + 1) == 0:
            solArr.append(ln + 1)
            continue

    answer += len(solArr)
#################################################################################
####################### NOT RESOLVED!!!!!!!!!!!!!!!!!!!!! #######################
#################################################################################
    return answer


print(solution(5, [2, 4], [1, 3, 5]))

