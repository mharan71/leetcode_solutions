# Intersection of Two Arrays

# Easy

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.


# In O(m+min(m,k) time and OO(m+min(m,k)) memory (size of arrays)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums_set = set(nums1)

        nums_inter = nums_set.intersection(nums2)

        return list(nums_inter)

# In O(n) time and O(m + k) memory (size of arrays)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums = []
        seen = set()

        for num in nums1:
            if num not in seen:
                seen.add(num)
        
        for num in nums2:
            if num in seen:
                nums.append(num)
        return list(set(nums))