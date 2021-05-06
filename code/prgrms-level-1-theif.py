def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    for re in reserve:
        a = lost.count(re - 1)
        b = lost.count(re + 1)

        if a == 1:
            lost.remove(re - 1)
            answer += 1
        elif b == 1:
            lost.remove(re + 1)
            answer += 1
#################################################################################
####################### NOT RESOLVED!!!!!!!!!!!!!!!!!!!!! #######################
#################################################################################
    return answer


print(solution(5, [2, 4], [1, 3, 5]))

