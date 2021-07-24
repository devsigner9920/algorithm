text = input()

text_list = []
tag_list = []

is_valid = True
valid_text = ''

tag_index = 0
for spell in text:
    if spell in ['<', '>']:
        tag_list.append(tag_index)
    tag_index += 1

for i in range(0, len(tag_list), 2):
    #print(tag_list[i], tag_list[i + 1])
    valid_text += text[:tag_list[i]][::-1] + text[tag_list[i]:tag_list[i + 1] + 1]
    print(valid_text)
    text = text[tag_list[i + 1] + 1:]
    print(text)
    if i == 0: break

print(valid_text)
