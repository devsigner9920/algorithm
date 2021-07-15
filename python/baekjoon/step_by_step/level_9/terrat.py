from math import sqrt

# x1, y1, r1, x2, y2, r2
# 0 , 1 , 2 , 3 , 4 , 5
t = int(input())

for _ in range(t):
    terrat = list(map(int, input().split()))

    d = 0 # 두 좌표 상의 거리

    dx = abs(terrat[0] - terrat[3])
    dy = abs(terrat[1] - terrat[4])

    r1, r2 = terrat[2], terrat[5]

    d = sqrt(dx**2 + dy**2) # 두 좌표의 x, y 위상이 다 다를 경우 두 점 사이의 거리는 피타고라스의 정리로 알 수 있다.

    if d == 0 and r1 == r2:
        print(-1)
        continue
    
    if abs(r1 - r2) == d or r1 + r2 == d:
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    else:
        print(0)
