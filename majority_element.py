# 169. Majority Element

# Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.


#  In O(n) time and O(n) memory

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        majority = n / 2

        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
       
        for val, count in nums_map.items():
            if count > majority:
                return val