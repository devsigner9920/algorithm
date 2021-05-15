def solution(s):
    answer = 0

    str_arr = list(s)

    stack_arr = []

    for st in str_arr:
        if len(stack_arr) == 0:
            stack_arr.append(st)
        else:
            if stack_arr[-1] == st:
                stack_arr.pop()
            else:
                stack_arr.append(st)
    
    answer = 0 if len(stack_arr) > 0 else 1

    return answer

print(solution('baabaa'))