def solution(s, n):
    answer = ''
    ans_arr = list(s)
    asc_lower = [i for i in range(ord('a'), ord('z') + 1)]
    asc_upper = [i for i in range(ord('A'), ord('Z') + 1)]

    for item in ans_arr:
        asc_item = ord(item)
        if asc_lower.count(asc_item):
            temp_idx = asc_lower.index(asc_item) + 1 + n
            if temp_idx > len(asc_lower):
                temp_idx = temp_idx - len(asc_lower) - 1
                answer += chr(asc_lower[temp_idx])
            else:
                answer += chr(asc_lower[temp_idx - 1])
            continue
        if asc_upper.count(asc_item):
            temp_idx = asc_upper.index(asc_item) + 1 + n
            if temp_idx > len(asc_upper):
                temp_idx = temp_idx - len(asc_upper) - 1
                answer += chr(asc_upper[temp_idx])
            else:
                answer += chr(asc_upper[temp_idx - 1])
            continue
        answer += item

    return answer


print(solution("a B z", 4))
