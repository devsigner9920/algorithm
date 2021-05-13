def solution(numbers, hand):
    answer = ''
    l_hand = 10
    r_hand = 12
    hand_arr = []
    
    for num in numbers:
        if num % 3 == 1:
             hand_arr.append('L')
             l_hand = num
        elif num % 3 == 2:
            loc_num = num if num != 0 else 11
            l_loc = 0
            if l_hand % 3 == 2:
                l_loc = abs(l_hand - loc_num) / 3
            else:
                temp_l_loc = loc_num - l_hand
                l_loc = (abs(temp_l_loc - 1) / 3) + 1 if temp_l_loc != 1 else 1
            
            r_loc = 0
            if r_hand % 3 == 2:
                r_loc = abs(r_hand - loc_num) / 3
            else:
                temp_r_loc = loc_num - (r_hand - 2)
                r_loc = (abs(temp_r_loc - 1) / 3) + 1 if temp_r_loc != 1 else 1
            
            if l_loc > r_loc:
                hand_arr.append('R')
                r_hand = loc_num
            elif l_loc < r_loc:
                hand_arr.append('L')
                l_hand = loc_num
            else:
                hand_str = str(hand).upper()[0]
                hand_arr.append(hand_str)
                if hand_str == 'L':
                    l_hand = loc_num
                else:
                    r_hand = loc_num
        elif num % 3 == 0:
            hand_arr.append('R')
            r_hand = num
    
    answer = ''.join(hand_arr)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))