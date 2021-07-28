n = int(input())
arr = list(map(int, input().split()))
result = [-1 for _ in range(n)]
stack = [0]
i = 1

while stack and i < n:
    while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()

    stack.append(i)
    i += 1

print(result)


