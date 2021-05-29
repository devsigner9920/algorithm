sugar = int(input())

x, y = 3, 5
cnt = 0
while sugar >= x or sugar >= y:
    y_div = divmod(sugar, y)
    if y_div[1] == 0:
        cnt += y_div[0]
        sugar = 0
        break
    sugar -= x
    cnt += 1

if sugar > 0:
    print(-1)
else:
    print(cnt)