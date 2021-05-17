import re


def solution(new_id):
    answer = ''
    answer = new_id.lower()
    answer = re.sub('[^a-z | 0-9 | \. | _ | -]', '', answer)
    answer = re.sub('\\.{2,}', '', answer)
    answer = re.sub('^\.|\.$', '', answer)
    answer = 'a' if answer == '' else answer
    answer = re.sub('^\.|\.$', '', answer[:15])
    while len(answer) < 3:
        answer += answer[len(answer) - 1]

    return answer


print(solution('z-+.^.'))
