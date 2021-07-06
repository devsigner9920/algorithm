# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

m, n = map(int, input().split())

prime_num_list = [True] * (n + 1)

def find_prime_num(num):
    for i in range(int(num ** 0.5) + 1):
        if i < 2:
            prime_num_list[i] = False
        
        if prime_num_list[i]:
            for j in range(i + i, num + 1, i):
                prime_num_list[j] = False

find_prime_num(n)

for i in range(m, n + 1):
    if prime_num_list[i]:
        print(i)