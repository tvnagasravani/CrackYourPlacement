from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        min_pos = 0
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
                min_pos = i
        max_profit = 0
        for i in range(min_pos + 1, len(prices)):
            if prices[i] - mini > max_profit:
                max_profit = prices[i] - mini
        
        return max_profit
