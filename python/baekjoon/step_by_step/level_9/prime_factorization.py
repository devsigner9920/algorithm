num = int(input())

def get_prime_num(n):
    if n == 1:
        return
    
    prime_list = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if prime_list[i]:
            for j in range(i + i, n + 1, i):
                prime_list[j] = False
    
    prime_numbers = []
    for i in range(len(prime_list)):
        if i > 1:
            if prime_list[i]:
                prime_numbers.append(i)
    return prime_numbers

def get_prime_factorization_list(prime_list, n):
    while n != 1:
        for i in prime_list:
            x, y = divmod(n, i)
            if y == 0:
                n = x
                print(i)
                break

get_prime_factorization_list(get_prime_num(num), num)
