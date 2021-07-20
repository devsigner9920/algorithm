t = int(input())

for _ in range(t):
    str_list = input().split()
    for i in range(len(str_list)):
        str_list[i] = str_list[i][::-1]
    print(' '.join(str_list))
