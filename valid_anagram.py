# 242. Valid Anagram

# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# In O(n) time and O(n) memory

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] += 1
                
        if s_map == t_map:
            return True
        
        return False