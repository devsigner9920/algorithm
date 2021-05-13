def is_prime_number(n):
    for i in range(2, n + 1):
        if i == n:
            return True
        else:
            if n % i == 0:
                return False

def solution(nums):
    answer = 0
    nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                prime_num = nums[i] + nums[j] + nums[k]
                print(prime_num)
                if is_prime_number(prime_num):
                    answer += 1

    return answer


print(solution([1,2,7,6,4]))