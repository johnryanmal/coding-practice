# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

from functools import cache


def test(func):
    cases = [
        [],
        [1],
        [2,4,6,2,5],
        [5,1,1,5]
    ]
    answers = [
        0,
        1,
        13,
        10
    ]
    
    for case, answer in zip(cases, answers):
        result = func(case.copy())
        assert result == answer, f'Solution "{func.__name__}" has wrong answer for case {case}, got {result}'
    print(f'Solution "{func.__name__}" passed all tests"')


# O(n) time
# O(n) space
def cached(nums):
    
    @cache
    def dp(i):
        if i >= len(nums):
            return 0
        
        return max(nums[i] + dp(i+2), dp(i+1))
    
    return dp(0)

# O(n) time
# O(1) space
def optimized(nums):
    highest = 0
    for i in range(len(nums)-1,-1,-1):
        num0 = nums[i]
        num1 = nums[i+1] if i+1 < len(nums) else 0
        num2 = nums[i+2] if i+2 < len(nums) else 0
        maxima = max(num0+num2, num1)
        nums[i] = maxima
        highest = max(highest, maxima)
    
    return highest



test(cached)
test(optimized)
