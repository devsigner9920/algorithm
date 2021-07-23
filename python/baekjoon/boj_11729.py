def hanoi(n, frm, to, sub):
    if n == 1:
        print(frm, to)
        return

    hanoi(n - 1, frm, sub, to)
    print(frm, to)
    hanoi(n - 1, sub, to, frm)


input_n = int(input())
print(2**input_n - 1)
hanoi(input_n, 1, 3, 2)