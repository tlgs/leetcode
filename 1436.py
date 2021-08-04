"""1436. Destination City

tags: set
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = set(), set()
        for (x, y) in paths:
            a.add(x)
            b.add(y)

        return (b - a).pop()
