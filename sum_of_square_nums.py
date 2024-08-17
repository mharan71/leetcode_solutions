# Sum of Square Numbers

# Medium

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
       
        a = 0
        b = int(sqrt(c))

        while a <= b:
            z = a*a + b*b
            if z == c:
                return True
            elif z < c:
                a+=1
            else:
                b-=1
    
        return False



# O(c) (from O(sqrt(c)^2 simplfied))

# if c == 1 or c == 0:
        #     return True
        # sqrt_c = int(sqrt(c)+1)
        # for i in range(sqrt_c):
        #     for z in range(1, sqrt_c):
        #         if i*i + z*z == c:
        #             return True

        # return False 