def solution(n):
    cnt = [True] * (n + 1)
    c = 0
    for i in range(2, int(n ** 0.5) + 1):
        if cnt[i] == True:  # 만약 소수면
            print(c)