def solution(d, budget):
    answer = 0
    current_price = 0

    d.sort()
    for i in range(len(d)):
        current_price += d[i]
        if current_price <= budget:
            answer += 1
        else:
            break

    return answer


print(solution([1, 3, 2, 5, 4], 9))
