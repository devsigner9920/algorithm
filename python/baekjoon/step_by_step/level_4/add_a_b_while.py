from sys import stdin

while 1:

    try:
        a, b = map(int, stdin.readline().rstrip().split())
        print('%d' % (a + b))
    except:
        break
