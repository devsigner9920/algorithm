def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisor = []
        for j in range(1, i + 1):
            if divisor.count(j):
                break
            q = i // j
            
            if i % j == 0:
                divisor.append(j)
                if j != q:
                    divisor.append(q)
        if len(divisor) % 2 == 0:
            answer += i
        else:
            answer -= i
        print(divisor)
    return answer

solution(13, 17)