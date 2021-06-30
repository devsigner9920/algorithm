t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    distance = y - x # 거리
    
    if distance <= 3:
        print(distance)
        continue
    
    sqrt_n = int(distance ** 0.5)
    n = sqrt_n ** 2
    m = int(distance ** 0.5) ** 2 + sqrt_n
    count = 2 * sqrt_n - 1

    if sqrt_n ** 2 == distance:
        print(count)
    elif n < distance <= m:
        print(count + 1)
    elif m < distance:
        print(count + 2)