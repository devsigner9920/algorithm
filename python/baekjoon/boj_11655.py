line = list(input())

for i in range(len(line)):
    s = line[i]
    if s.isupper():
        pos = ord(s) + 13
        if pos > 90:
            line[i] = chr(pos - 26)
        else:
            line[i] = chr(pos)
    elif s.islower():
        pos = ord(s) + 13

        if pos > 122:
            line[i] = chr(pos - 26)
        else:
            line[i] = chr(pos)
    else:
        continue

print(''.join(line))