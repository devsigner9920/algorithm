from sys import stdin

a = stdin.readline().rstrip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cro:
    a = a.replace(c, '_')

print(len(a))