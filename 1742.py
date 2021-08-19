"""1742. Maximum Number of Balls in a Box

Given the constraints, an array is a reasonable alternative to a dictionary.

difficulty: easy
tags: array
runtime: 99.39
memory: 55.64
"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = [0] * 46

        first, t = lowLimit, 0
        while first:
            t += first % 10
            first //= 10

        counts[t] = 1

        for ball in range(lowLimit + 1, highLimit + 1):
            while ball % 10 == 0:
                t -= 9
                ball //= 10

            t += 1
            counts[t] += 1

        return max(counts)
