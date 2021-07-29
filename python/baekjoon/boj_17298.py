n = int(input())
nums = list(map(int, input().split()))
stack = [0]
result = [-1 for _ in range(n)]

for i in range(1, n):
    while stack:
        if nums[stack[-1]] < nums[i]:
            tmp = stack.pop()
            result[tmp] = nums[i]
        else:
            break

    stack.append(i)


print(' '.join(map(str, result)))