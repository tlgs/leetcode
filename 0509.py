"""509. Fibonacci Number

difficulty: easy
tags: dynamic programming
"""


class Solution:
    mem = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n not in self.mem:
            self.mem[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.mem[n]
