t = int(input())

num = 10000
seive = [False, False] + [True] * (num - 1)

for i in range(2, int(num ** 0.5) + 1):
    if i < 2: seive[i] = False
    if seive[i]:
        for j in range(i + i, num + 1, i):
            seive[j] = False

seive_num_list = [i for i, val in enumerate(seive) if val]

for _ in range(t):
    n = int(input())

    q, r = divmod(n, 2)
    if r == 0 and seive[q]:
        print(q, q)
        continue

    ans_n = 0
    ans_m = 9999
    for k in seive_num_list:
        if n < k: break
        ans = n - k
        if seive[ans]:
           if abs(ans_n - ans_m) >= abs(k - ans):
               ans_n = ans
               ans_m = k
    
    print(ans_n, ans_m)