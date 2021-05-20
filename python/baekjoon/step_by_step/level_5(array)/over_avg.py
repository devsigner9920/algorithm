from sys import stdin

c = int(stdin.readline().rstrip())

for _ in range(c):
    avg_list = list(map(int, stdin.readline().rstrip().split()))
    student_num = avg_list.pop(0)
    avg = sum(avg_list) / student_num
    over_avg_list = [stu for stu in avg_list if stu > avg]
    print('{:.3f}%'.format(round(len(over_avg_list) / len(avg_list) * 100, 3)))