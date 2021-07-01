# 여러 개의 숫자 카드 중에서
# 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 1. 숫자가 쓰인 카드들이 n * m 형태로 놓여 있다.
#   n은 행의 개수를 의미
#   m은 열의 개수를 의미
# 2. 뽑고자 하는 카드가 포함되어 있는 행 선택
# 3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.

# 입력 조건
# 첫째 줄에 행열 n, m(1 <= n, m <= 100)
# 둘째 줄 부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다.
# 각 숫자는 1 이상 10000 이하의 자연수

# 출력 조건
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

n, m = map(int, input().split())

result = 0
for _ in range(n):
    data = sorted(list(map(int, input().split()))) # 열 데이터 입력 및 공백으로 자른 후 정렬된 리스트화
    min_num = data[0] # 해당 리스트에서 가장 작은 수
    # print("min num:", min_num)
    if result < min_num: # 만약 결과값보다 min_num이 크다면 min_num으로 결과값 대치
        result = min_num

print(result)