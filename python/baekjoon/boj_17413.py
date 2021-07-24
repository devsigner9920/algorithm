text = input()
valid_text = ''

while text:
    start = text.find('<')
    end = text.find('>')

    if start != -1:
        valid_text += ' '.join(list(map(lambda x: x[::-1], text[:start].split()))) + text[start:end + 1]
        text = text[end + 1:]
    else:
        valid_text += ' '.join(list(map(lambda x: x[::-1], text.split())))
        break

print(valid_text)