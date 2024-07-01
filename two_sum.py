# Two Integer Sum

# Easy

#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.


# In O(n)

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in num_map:
                return [num_map[diff], index]
            num_map[value] = index
        


# In O(n^2)

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        sum_lst = []
        
        for z in range(len(nums)):
            for i in range(z + 1, len(nums)):
                if nums[z] + nums[i] == target:
                    sum_lst.append(z)
                    sum_lst.append(i)
        return sum_lst