from sys import stdin

def a(n):
    answer = 0
    for i in range(1, n + 1):
        if i < 100:
            answer += 1
            continue
        
        num_list = list(str(i))
        gap_set = set()
        for j in range(1, len(num_list)):
            gap_set.add(int(num_list[j]) - int(num_list[j - 1]))
        
        if len(gap_set) > 1:
            continue
        else:
            answer += 1
        
    return answer

print(a(int(stdin.readline().rstrip())))