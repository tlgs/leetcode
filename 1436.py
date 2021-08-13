"""1436. Destination City

difficulty: easy
tags: set
runtime: 75.68
memory: 92.23
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = set(), set()
        for (x, y) in paths:
            a.add(x)
            b.add(y)

        return (b - a).pop()
