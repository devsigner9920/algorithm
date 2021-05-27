from sys import stdin

num = int(stdin.readline().rstrip())

cnt = 0
stack_num = 0
while stack_num < num:
    cnt += 1
    stack_num += cnt

up_down = True if cnt % 2 == 0 else False
seq = num - (stack_num - cnt)
if up_down:
    print('%d/%d' % (seq, cnt + 1 - seq))
else:
    print('%d/%d' % (cnt + 1 - seq, seq))