def solution(s):
    answer = 0
    result = ''
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    word = '';
    for i in range(len(s)):
        if s[i].isnumeric(): result += s[i]
        else:
            word += s[i]
            if word in num_dict:
                result += str(num_dict[word])
                word = ''

    answer = int(result)
    
    return answer


solution("one4seveneight")