def solution(n, k, cmd):
    answer = ''
    del_arr = []
    res_arr = ['O'] * n
    
    for c in cmd:
        c_arr = c.split(' ')
        if c_arr[0] == 'U':
            k -= int(c_arr[1])
        elif c_arr[0] == 'D':
            k += int(c_arr[1])
        elif c_arr[0] == 'C':
            del_arr.append(k)
            res_idx = k
            for del_num in del_arr:
                if del_num < k:
                    res_idx += 1
            res_arr[res_idx] = 'X'
            if k == n - 1:
                k -= 1
        elif c_arr[0] == 'Z':
            recovery = del_arr.pop()
            res_arr[recovery] = 'O'
            if recovery < k:
                k += 1
        print('command : ' + c)
        print('cursor : ' + str(k))
        print('result : ' + ''.join(res_arr))
        print(del_arr)
    answer = ''.join(res_arr)
    print(answer)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
