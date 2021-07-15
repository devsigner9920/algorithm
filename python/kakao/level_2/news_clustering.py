def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()

    list1 = []
    for i in range(1, len(str1)):
        temp_str = str1[i - 1] + str1[i]
        if temp_str.isalpha():
            list1.append(temp_str)
    
    list2 = []
    for i in range(1, len(str2)):
        temp_str = str2[i - 1] + str2[i]
        if temp_str.isalpha():
            list2.append(temp_str)
    
    elem_dict1 = {}
    elem_dict2 = {}

    for elem in list1:
        elem_dict1[elem] = list1.count(elem)
    
    for elem in list2:
        elem_dict2[elem] = list2.count(elem)
    

    cross = set(list1) & set(list2)

    cross_num = 0;
    union_num = 0;
    for elem in list(cross):
        cross_num += min(elem_dict1[elem], elem_dict2[elem])
        union_num += max(elem_dict1[elem], elem_dict2[elem])
    
    
    for elem in list(set(list1) - set(list2)):
        union_num += elem_dict1[elem]
    
    
    for elem in list(set(list2) - set(list1)):
        union_num += elem_dict2[elem]
    
    if union_num == 0:
        return 65536

    answer = int((cross_num / union_num) * 65536)
    return answer

print(solution('handshake', 'shake hands'))