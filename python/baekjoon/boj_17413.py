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


# 참조코드
# s=list(input())
# tag=False
# word=''
# result=''
# for i in s:
#   #뒤집어서 출력
#   if tag==False:
#     if i=='<':
#       tag=True
#       word=word+i
#     #중간점검
#     elif i==' ':
#       word=word+i
#       result=result+word
#       word=''
#     else:
#       word=i+word
#
#   #정상적으로 출력
#   elif tag==True:
#     word=word+i
#     if i=='>':
#       tag=False
#       result=result+word
#       word=''
#
# print(result+word)