t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    n = int(input().rstrip())

    memo = [[0 for _ in range(n)] for _ in range(k + 1)]
    for i in range(k + 1):
        for j in range(1, n + 1):
            if i == 0:
                memo[i][j - 1] = j
                continue
            memo[i][j - 1] = sum(memo[i - 1][:j])
    
    print(memo.pop().pop())