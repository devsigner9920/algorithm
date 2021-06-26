n = int(input())
num_list = list(map(int, input().split()))

def find_prime_num(numbers):
    max_num = max(numbers)
    prime_num_list = [True] * (max_num + 1)
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if prime_num_list:
            for j in range(i + i, max_num + 1, i):
                prime_num_list[j] = False
    cnt = 0
    for num in num_list:
        if num < 2:
            continue
        if prime_num_list[num]:
            cnt += 1
    return cnt


print(find_prime_num(num_list))