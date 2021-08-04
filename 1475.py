"""1475. Final Prices With a Special Discount in a Shop

tags: monotonic stack
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack.pop()] -= p
            stack.append(i)

        return prices
