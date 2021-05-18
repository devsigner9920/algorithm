def solution(rows, columns, queries):
    answer = []
    mat = [[i * j for j in range(1, columns * i + 1)] for i in range(1, rows + 1)]
    print(mat)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100,97,[[1,1,100,97]]))