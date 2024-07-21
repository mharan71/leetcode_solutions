# Validate Parentheses

# Easy

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

#The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.


# In O(n) time and space

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        valid_dic = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char not in valid_dic:
                stack.append(char)
                continue
            if not stack or stack[-1] != valid_dic[char]:
                return False
            stack.pop()
        return not stack
    
