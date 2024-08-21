# 485. Max Consecutive Ones

# Easy 

# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# In O(n) time and O(1) memory

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
            
        return max_count


# In O(n) time and O(n) memory

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        lst = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
                lst.append(count)
            else:
                count = 0
                lst.append(count)
        return max(lst)
