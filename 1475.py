"""1475. Final Prices With a Special Discount in a Shop"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        The use of a stack allows for this problem to be solved in a single pass.

        Instead of looking ahead to find the next smaller value, we keep track of values
        seen previously and backtrack to apply the discount if applicable.
        """
        stack = []
        for i, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack.pop()] -= p
            stack.append(i)

        return prices
