
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def has_twosum(nums, k):
    complements = set()
    for num in nums:
        if num in complements:
            return True
        else:
            complements.add(k - num)
    return False

print(has_twosum([10, 15, 3, 7], 17))