def solution(n):
    answer = 0
    count_num = "{0:b}".format(n).count('1')

    i = n + 1
    while True:
        trg_num = "{0:b}".format(i).count('1')
        if trg_num == count_num:
            break
        else:
            i += 1
    return i

