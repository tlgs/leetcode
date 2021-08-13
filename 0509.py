"""509. Fibonacci Number

difficulty: easy
tags: dynamic programming
runtime: 83.18
memory: 89.45
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        prev, curr = 0, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr

        return curr
