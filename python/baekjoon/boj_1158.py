n, k = map(int, input().split())

nums = [i for i in range(1, n + 1)]
result = []

i = k - 1
while len(nums):
    if i < len(nums):
        result.append(nums.pop(i))
        i += (k - 1)
    else:
        i = i - len(nums)


print('<' + ', '.join(map(str, result)) + '>')
