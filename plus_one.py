# Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit 
# of the integer. The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# O(n) time

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = str(int("".join(map(str, digits))) + 1)
        digits.clear()
        for i in number:
            digits.append(int(i))

        return digits
    
# O(n) time

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits