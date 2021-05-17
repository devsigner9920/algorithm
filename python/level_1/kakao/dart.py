def solution(dartResult):
    answer = 0
    ans_arr = [''] * 3
    pos = 0
    score_dict = {'S': 1, 'D': 2, 'T': 3}
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            ans_arr[pos] += dartResult[i]
        elif dartResult[i].isalpha():
            ans_arr[pos] = int(ans_arr[pos]) ** score_dict[dartResult[i]]
            pos += 1
        elif not (dartResult[i].isnumeric() and dartResult[i].isalpha()):
            print(dartResult[i])
            if dartResult[i] == '*':
                ans_arr[pos - 1] = ans_arr[pos - 1] * 2
                if pos != 1:
                    ans_arr[pos - 2] = ans_arr[pos - 2] * 2
            else:
                ans_arr[pos - 1] = ans_arr[pos - 1] * -1

    return sum(ans_arr)


print(solution('1S*2T*3S'))

