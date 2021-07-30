from sys import stdin

n = int(stdin.readline().rstrip())
persons = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
result = []
for i in range(n):
    src = persons.pop(i)
    grade = 1
    for j in range(n - 1):
        if src[0] < persons[j][0] and src[1] < persons[j][1]:
            grade += 1
    result.append(grade)
    persons.insert(i, src)

print(' '.join(map(str, result)))
