"""830. Positions of Large Groups (EASY)

tags: itertools
"""


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        idx, res = 0, []
        for _, g in itertools.groupby(s):
            x = len(list(g))
            if x >= 3:
                res.append([idx, idx + x - 1])
            idx += x

        return res
