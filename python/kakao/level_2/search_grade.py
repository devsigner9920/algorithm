from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dic = defaultdict(list)
    for inf in info:
        inf = inf.split()
        inf_key = inf[:-1]
        inf_val = int(inf[-1])
        for i in range(5):
            for c in combinations(inf_key, i):
                tmp_key = ''.join(c)
                info_dic[tmp_key].append(inf_val)

    for key in info_dic.keys():
        info_dic[key].sort()

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]

        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)


    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
