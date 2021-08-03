s = input()

s_dict = {chr(i): 0 for i in range(97, 123)}

for a in s:
    s_dict[a] += 1

print(' '.join(map(str, (s_dict.values()))))