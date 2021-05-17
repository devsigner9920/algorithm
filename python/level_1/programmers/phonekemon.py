def solution(nums):
    answer = 0
    non_dup_nums = list(set(nums))
    answer = (len(nums) / 2) if (len(non_dup_nums) > (len(nums) / 2)) else len(non_dup_nums)
    return answer


test_case_1 = [3, 1, 2, 3]
test_case_2 = [3, 3, 3, 2, 2, 4]
test_case_3 = [3, 3, 3, 2, 2, 2]

solution(test_case_1)
solution(test_case_2)
solution(test_case_3)

