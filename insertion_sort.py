# Insertion Sort

# Easy

# Given a list of key-value pairs, sort the list by key using Insertion Sort. 
# Return a list of lists showing the state of the array after each insertion. 
# If two key-value pairs have the same key, maintain their relative order in the sorted list.




# In O(n^2) time and O(n) memory

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertion_sort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        if pairs == []:
            return pairs
        result.append(pairs[:])

        for i in range(1, len(pairs)):
            j = i - 1

            while j>= 0 and pairs[j].key > pairs[j+1].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -=1
            result.append(pairs[:])
        return result