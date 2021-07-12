from math import sqrt

# x1, y1, r1, x2, y2, r2
# 0 , 1 , 2 , 3 , 4 , 5
t = int(input())

for _ in range(t):
    terrat = list(map(int, input().split()))

    d = 0 # 두 좌표 상의 거리

    dx = abs(terrat[0] - terrat[3])
    dy = abs(terrat[1] - terrat[4])

    if dx == 0: # x 좌표가 같은 경우
        d = dy
    if dy == 0: # y 좌표가 같은 경우
        d = dx

    if d == 0 and terrat[2] == terrat[5]:
        print(-1)
        continue
    
    if d == 0:
        d = sqrt(dx**2 + dy**2) # 두 좌표의 x, y 위상이 다 다를 경우 두 점 사이의 거리는 피타고라스의 정리로 알 수 있다.

    large_r, small_r = 0, 0
    if terrat[2] > terrat[5]:
        large_r, small_r = terrat[2], terrat[5]
    else:
        large_r, small_r = terrat[5], terrat[2]

    if large_r - small_r < d < small_r + large_r:
        print(2)
    if large_r + small_r == d:
        print(1)
    if large_r + small_r < d or d == 0:
        print(0)
