from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
nums_count = dict(Counter(nums))
stack = [0]
result = [-1 for _ in range(n)]

for i in range(1, n):
    while stack:
        if nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
        else:
            break
    stack.append(i)

print(' '.join(map(str, result)))