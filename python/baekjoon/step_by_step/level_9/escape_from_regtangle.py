x, y, w, h = map(int, input().split()) # (x, y): 직사각형 내에서의 위치, (w, h): 직사각형의 크기

print(min(x, y, w - x, h - y))