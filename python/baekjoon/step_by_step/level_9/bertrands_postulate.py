# 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용
# n < x <= 2n

num = 123456 * 2

prime_num_list = [True] * (num + 1)


for i in range(int(num ** 0.5) + 1):
    if i < 2: prime_num_list[i] = False

    if prime_num_list[i]:
        for j in range(i + i, num + 1, i):
            prime_num_list[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(map(lambda x : x, prime_num_list[n + 1:(2 * n) + 1])))