def solution(name):
    answer = 0

    alphabet_list = [i for i in range(ord('A'), ord('Z') + 1)]
    n_seq = []
    name_list = list(name)

    for i in range(len(name_list)):
        print(name_list[i])
        if not len(n_seq):
            n_seq.append(i)
            continue
        
        last_pos = n_seq[-1]
        next_goal = name_list.index('A', n_seq[-1] + 1)
        print(next_goal)

    for i in n_seq:
        literal = name[i]
        if literal == 'A':
            continue
        
        l_tick = len(alphabet_list) - alphabet_list.index(ord(literal))
        r_tick = alphabet_list.index(ord(literal))
        answer += l_tick if l_tick > r_tick else r_tick
    
    return answer


solution("JAN")
