# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

from functools import reduce
from itertools import accumulate
from operator import mul

def product(nums):
    return reduce(mul, nums)

def solution(nums):
    prod = product(nums)
    return [prod//num for num in nums]

def follow_up_naive(nums):
    return [product(nums[:i]+nums[i+1:]) for i in range(len(nums))]

def r_accumulate(iterable, *args, **kwargs):
    return reversed(tuple(accumulate(reversed(iterable), *args, **kwargs)))

def follow_up(nums):
    leftprod = list(accumulate([1]+nums[:-1], mul))
    rightprod = list(r_accumulate(nums[1:]+[1], mul))
    return [left*right for left, right in zip(leftprod, rightprod)]


print(solution([1,2,3,4,5]))
print(follow_up_naive([1,2,3,4,5]))
print(follow_up([1,2,3,4,5]))