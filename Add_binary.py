# Add Binary

# Easy

# Given two binary strings a and b, return their sum as a binary string.



# In O(n+m) time and O(n+m) space

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int(a,2), int(b,2)
        result = a + b
        return bin(result)[2:]