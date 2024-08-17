# Counting Bits

# Easy

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

# In O(N) Time and O(N) memory

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the array with zeros
        dp = [0] * (n + 1)
        
        # Iterate over the range from 1 to n
        for i in range(1, n + 1):
        
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp


# In O(N^2) time and O(nlogn) memory

class Solution:
    def countBits(self, n: int) -> List[int]:

        # Initialize empy array for binary numbers
        binary_arr = []
        # Initialize empy array for count of 1's
        count_arr = []

        # Iterate over 1 to n
        for i in range(n+1):
            # Append binary number to array
            binary_arr.append((bin(i)[2:]))
        
        # Iterate over numbers in binary_arr
        for number in binary_arr:
            count = 0
            # Iterate over digits
            for digit in number:
                # If digit it one increase the count
                if digit == "1":
                    count +=1
            # Append count to count_arr
            count_arr.append(count)
        return count_arr