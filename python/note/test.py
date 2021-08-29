# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    S = list(S)
    results = []
    for i in range(len(S)):
        tmp = S.pop(i)
        results.append(''.join(S))
        S.insert(i, tmp)

    results = sorted(results)
    return results[0]
print(solution('codility'))