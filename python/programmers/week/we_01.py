def solution(price, money, count):
    n = price * sum([i for i in range(1, count + 1)])
    if n < money: return 0
    return n - money
