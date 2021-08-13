"""322. Coin Change

difficulty: medium
tags: dynamic programming
runtime: 94.71
memory: 81.49
"""
import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [sys.maxsize for _ in range(amount)]
        for value in range(1, amount + 1):
            for coin in coins:
                if value >= coin:
                    if dp[value - coin] + 1 < dp[value]:
                        dp[value] = dp[value - coin] + 1

        return dp[-1] if dp[-1] != sys.maxsize else -1
