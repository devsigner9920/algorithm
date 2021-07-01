# 1이 될 때까지
# 어떤수 n이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행
# 단, 두 번째 연산은 n이 k로 나누어떨어질 때만 선택할 수 있다.
# 1. n - 1
# 2. n / k

n, k = map(int, input().split())

result = 0
# my source start
"""
while n != 1:
    if n % k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1
"""
# my source end

while True:
    target = (n // k) * k # 몫 곱하기 k 는 나눌 수 있는 n과 가장 가까운 수를 구할 수 있다.
    result += (n - target) # 1만큼 빼야할 상황에 반복문을 사용하지 않고 1만큼 뺀 횟수를 구할 수 있다.
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1) # 예를 들어 4가 남았을 때, 나눌 수 없는 상황에서 잔여 찌꺼기 처리하는 모양이 나온다.

print(result)