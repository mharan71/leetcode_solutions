# Is Palindrome

# Easy

# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.


# In O(n) (6 * n)

class Solution:
    def is_palindrome(self, s: str) -> bool:
       
        char_lst = [i for i in s if i.isalnum()]
        char_lst = char_lst[::-1]
        word_reversed = "".join(char_lst)
        char_lst_2 = [i for i in s if i.isalnum()]
        word = "".join(char_lst_2)

        return word.lower() == word_reversed.lower()

