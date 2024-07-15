# Buy and Sell Crypto

#Easy

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.



# In O(n)

class Solution:
    def max_profit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        max_prof = 0
        min_price = prices[0]

        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price > max_prof:
                max_prof = price - min_price
        return max_prof


# In O(n)

class Solution:
    def max_profit(self, prices: List[int]) -> int:

        max_prof = 0
        min_price = prices[0]
        for price in prices:
            if min_price > price:
                min_price = price
            max_prof = max(max_prof, price - min_price)
        return max_prof



# In O(n^2)

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        lst = []
        
        if len(prices) == 0 or len(prices) == 1:
            return 0

        for i in range(len(prices)):
            for z in range(i+1, len(prices)):
                value = prices[z] - prices[i]
                lst.append(value)
        
        high = max(lst)
        if high < 0:
            return 0
        return high