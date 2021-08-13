"""1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

difficulty: medium
tags: greedy
runtime: 61.34
memory: 46.54
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        mem = [1, 1]
        while mem[-1] < k:
            mem.append(mem[-1] + mem[-2])

        result = 0
        while k:
            if k >= mem[-1]:
                result += 1
                k -= mem[-1]
            else:
                mem.pop()

        return result
