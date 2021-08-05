s = input()
s_list = sorted([s[i:] for i in range(len(s))])
for t in s_list: print(t)