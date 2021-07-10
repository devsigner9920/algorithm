from collections import Counter

def get_point(_list) -> int:
    return list(filter(lambda x : x[1] == 1, Counter(_list).items()))[0][0]

x_list, y_list = [], []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

print(get_point(x_list), get_point(y_list))