def solution(numbers, hand):
    answer = ''
    num_dict = {}
    l_loc = 10
    r_loc = 12
    for i in range(1, 5):
        k = i - 1
        l = 0
        for j in range(3 * i - 2, 3 * i + 1):
            num_dict[j] = (k, l)
            l += 1

    for num in numbers:
        proc_num = num if num != 0 else 11

        if proc_num % 3 == 1: # 1 4 7
            answer += 'L'
            l_loc = proc_num
        elif proc_num % 3 == 2: # 2 5 8
            l_distance = abs(num_dict[l_loc][0] - num_dict[proc_num][0]) + abs(num_dict[l_loc][1] - num_dict[proc_num][1])
            r_distance = abs(num_dict[r_loc][0] - num_dict[proc_num][0]) + abs(num_dict[r_loc][1] - num_dict[proc_num][1])
            if l_distance > r_distance:
                answer += 'R'
                r_loc = proc_num
            elif l_distance < r_distance:
                answer += 'L'
                l_loc = proc_num
            else:
                hand_upper = hand[0].upper()
                answer += hand_upper
                if hand_upper == 'L':
                    l_loc = proc_num
                else:
                    r_loc = proc_num
        elif proc_num % 3 == 0: # 3 6 9
            answer += 'R'
            r_loc = proc_num
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
