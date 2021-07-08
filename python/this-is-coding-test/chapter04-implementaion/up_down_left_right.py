# 여행가 A는 n * n 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (n, n)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# 입력 예시
# 5
# R R R U D D
x, y = 1, 1
n = int(input())
plan_list = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plan_list: # 플랜리스트 만큼 반복
    for i in range(len(move_types)):
        # 이동 후 좌표 구하기
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 범위 벗어날 경우 예외처리
    if nx == 0 or nx > n or ny == 0 or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

# for plan in plan_list:
#     if plan == "L":
#         tmp = x - 1
#         if tmp:
#             x = tmp
#     if plan == "R":
#         tmp = x + 1
#         if tmp <= n:
#             x = tmp
#     if plan == "U":
#         tmp = y - 1
#         if tmp:
#             y = tmp
#     if plan == "D":
#         tmp = y + 1
#         if tmp <= n:
#             y = tmp

print(x, y)