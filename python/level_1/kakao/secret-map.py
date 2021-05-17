def solution(n, arr1, arr2):
    answer = []

    for x, y in zip(arr1, arr2):
        bin_str = bin(x | y).replace('0b', '').replace('1', '#').replace('0', ' ')
        bin_str = bin_str if len(bin_str) == n else ' ' * (n - len(bin_str)) + bin_str

        answer.append(bin_str)

    return answer


print(solution(5, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
