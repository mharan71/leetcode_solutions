# Contains Duplicate

# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


# In O(n) time and O(n) memory

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        return False