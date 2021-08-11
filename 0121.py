"""121. Best Time to Buy and Sell Stock

difficulty: easy
tags: array
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, p = prices[0], 0
        for v in prices[1:]:
            if v < m:
                m = v

            if v - m > p:
                p = v - m

        return p
