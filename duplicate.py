# 26. Remove Duplicates from Sorted Array

# Easy

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.


# In O(n) time and O(n) memory

def remove(nums):
    if not nums:
        return 0
        
    seen = set()
    k = 0
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[k] = num
            k +=1

    return k