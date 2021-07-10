while True:
    x = sorted(list(map(int, input().split())))
    max_num = x.pop()
    if max_num == 0:
        break
    if max_num**2 == sum(map(lambda y: y * y, x)):
        print('right')
    else:
        print('wrong')