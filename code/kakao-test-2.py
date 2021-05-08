"""
맨해튼 거리
두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

맨해튼 거리 2이하 앉지마!
"""

def sol(place):
    p = []
    x = []
    for i in range(len(place)):
        arr = list(place[i])
        for j in range(len(arr)):
            tup = (i, j)
            if arr[j] == 'P':
                p.append(tup)
            elif arr[j] == 'X':
                x.append(tup)
    
    for i in range(len(p)):
        for j in range(i + 1, len(p) - 1):
            if 2 >= abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]):
                if p[i][0] != p[j][0] and p[i][1] != p[j][1]:
                    cnt = x.count((p[i][0] + 1, p[i][1])) + x.count((p[i][0], p[i][1] + 1))
                    if cnt != 2:
                        return 0
                elif p[i][0] != p[j][0]:
                    cnt = x.count((p[i][0] + 1, p[i][1]))
                    if cnt == 0:
                        return 0
                elif p[i][1] != p[j][1]:
                    cnt = x.count((p[i][0], p[i][1] + 1))
                    if cnt == 0:
                        return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(sol(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))