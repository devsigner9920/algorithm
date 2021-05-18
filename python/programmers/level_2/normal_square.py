def solution(w,h):
    answer = 1

    a = w
    b = h
    
    if a < b:
        temp = b
        b = a
        a = temp
    
    while b != 0:
        temp = a % b
        a = b
        b = temp
    

    rate_w = w / a
    rate_h = h / a
    
    answer = int(w * h - (rate_w + rate_h - 1) * a)


    return answer

print(solution(8, 12))