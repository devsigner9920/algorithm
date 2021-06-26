m = int(input())
n = int(input())

def find_prime_num(min_num, max_num):
    prime_num_list = [True] * (max_num + 1)
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if prime_num_list[i]:
            for j in range(i + i, max_num + 1, i):
                prime_num_list[j] = False
    
    prime_numbers = []
    for num in range(min_num, max_num + 1):
        if num < 2:
            continue
        if prime_num_list[num]:
            prime_numbers.append(num)
    
    if len(prime_numbers):
        print(sum(prime_numbers))
        print(min(prime_numbers))
    else:
        print(-1)


find_prime_num(m, n)