import string
import math

tmp = string.digits


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime_number(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    if k == 10:
        trans_num = str(n)
    else:
        trans_num = convert(n, k)


    prime_num_list = trans_num.split('0')
    for item in prime_num_list:
        if item == '': continue
        if is_prime_number(int(item)):
            answer += 1
    return answer


print(solution(110011, 10))
