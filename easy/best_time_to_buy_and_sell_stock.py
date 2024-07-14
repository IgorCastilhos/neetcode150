from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            if price < min_price:
                min_price = price

        return max_profit


# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(s.maxProfit([7, 6, 4, 3, 1]))  # 0
print(s.maxProfit([1, 2]))  # 1
print(s.maxProfit([2, 1]))  # 0
print(s.maxProfit([2, 4, 1]))  # 2
print(s.maxProfit([3, 2, 6, 5, 0, 3]))  # 4
