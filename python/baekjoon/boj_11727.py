n = int(input())

dp = [0, 1, 3, 5] + [0 for _ in range(n-2)]

if n <= 3:
    print(dp[n])
else :
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(dp[i] % 10007)