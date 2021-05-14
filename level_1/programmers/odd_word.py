def solution(s):
    answer = ''
    i = 0
    for idx in range(len(s)):
        answer += s[idx].upper() if i % 2 == 0 else s[idx].lower()
        i = i + 1 if s[idx] != ' ' else 0
    return answer


print(solution("try hello world"))
