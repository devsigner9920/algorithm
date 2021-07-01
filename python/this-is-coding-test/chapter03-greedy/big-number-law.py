# 큰 수의 법칙
# question
# 다양한 수로 이루어진 배일이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

# 입력 조건
# 첫째 줄
# - N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= 10000) 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄
# - N개의 자연수가 주어진다.
# - 각 자연수는 공백으로 구분한다.
# - 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
# - 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건
# 첫째줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = 5, 8, 3 # map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, list('24546'))) # list(map(int, input().split()))

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번쨰로 큰 수

result = 0

# low level code start
"""
while True: # m이 0이 될때까지 반복
    for i in range(k): # k 만큼 반복하여 제일 큰 수 더하기
        if m == 0: # m이 0일 경우 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 감소
    if m == 0: # m이 0이라면 while 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 감소

"""
# low level code end
# high quality code start
# k번 제일 큰 수 더하고, 한번 두 번째 큰 수 더하는 규칙
# 1회 루틴: k + 1

# 가장 큰 수가 더해지는 횟수: m // (k + 1) * k + M % (k + 1)
count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
