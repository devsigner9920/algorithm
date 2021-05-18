import datetime

WEEK = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def solution(a, b):
    answer = ''
    date = datetime.datetime(2016, a, b)

    answer = WEEK[date.weekday()]
    return answer


print(solution(5, 24))
