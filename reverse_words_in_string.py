# 151. Reverse Words in a String

# Medium

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.


# In O(n) time and O(n) space

class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.split()
        arr = arr[::-1]
        final_s = " ".join(arr)
        return final_s