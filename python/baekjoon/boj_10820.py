from sys import stdin


def analyze_string(s):
    s_list = [0 for _ in range(4)]
    for n in s:
        if n.isupper():
            s_list[1] += 1
        elif n.islower():
            s_list[0] += 1
        elif n.isnumeric():
            s_list[2] += 1
        elif n.isspace():
            s_list[3] += 1
    return ' '.join(map(str, s_list))


while True:
    st = stdin.readline().rstrip('\n')
    if st:
        print(analyze_string(st))
    else:
        break
