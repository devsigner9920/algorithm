# 여행가 A는 n * n 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (n, n)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# 입력 예시
# 5
# R R R U D D
data = {
    "x": 1,
    "y": 1,
    "L": -1,
    "R": 1,
    "U": -1,
    "D":1
}
#x, y = 1

n = int(input())
plan_list = list(map(int, input().split()))

for plan in plan_list:
    print(plan)