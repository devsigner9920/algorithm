STAT = {
    'Enter' : '님이 들어왔습니다.',
    'Leave' : '님이 나갔습니다.'
}


def solution(record):
    answer = []
    record_dict = {}
    for item in record:
        temp = item.split(' ')
        if temp[0] != 'Leave':
            record_dict[temp[1]] = temp[2]

        if temp[0] == 'Change':
            continue

        answer.append(temp[1] + STAT[temp[0]])

    for key in record_dict.keys():
        for i in range(len(answer)):
            answer[i] = answer[i].replace(key, record_dict[key])

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
