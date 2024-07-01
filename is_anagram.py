# Is Anagram

# Easy

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.



# Solution in O(n)

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        letters_1, letters_2 = {}, {}
        
        for char in s:
            if char not in letters_1:
                letters_1[char] = 0
            letters_1[char] += 1
            
        for char in t:
            if char not in letters_2:
                letters_2[char] = 0
            letters_2[char] += 1
        
        return letters_1 == letters_2



# Solution in O(n)

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_1, letters_2 = {}, {}

        for i in range(len(s)):
            letters_1[s[i]] = 1 + letters_1.get(s[i], 0)
            letters_2[t[i]] = 1 + letters_2.get(t[i], 0)
        return letters_1 == letters_2



# Solution in O(nlogn)

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        letters_1 = sorted([i for i in s])
        letters_2 = sorted([i for i in t])

        if letters_1 == letters_2:
            return True
        return False


# Solution in O(n^2) 

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:

        letters_1 = {char: s.count(char) for char in s}
        letters_2 = {char: t.count(char) for char in t}

        return letters_1 == letters_2


