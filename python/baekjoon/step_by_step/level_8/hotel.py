t = int(input())

for _ in range(t):
    y, x, m = map(int, input().split())
    room, floor = map(str, divmod(m, y))
    if int(floor):
        room = str(int(room) + 1)
    else:
        floor = str(y)
    room = room if len(room) > 1 else '0' + room
    print(floor + room)
