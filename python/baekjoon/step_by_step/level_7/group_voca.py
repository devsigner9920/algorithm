from sys import stdin

# t = int(stdin.readline().rstrip())

# no_group_voca = 0
# for _ in range(t):
#     tmp = stdin.readline().rstrip()
#     for idx, a in enumerate(tmp):
#         if tmp[idx + 1:].find(a) > 0:
#             no_group_voca += 1
#             break
# print(t - no_group_voca)

answer = 0
for _ in range(int(stdin.readline().rstrip())):
    tmp = stdin.readline().rstrip()
    if tmp == ''.join(sorted(tmp, key=tmp.find)):
        answer += 1
print(answer)