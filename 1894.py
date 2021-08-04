"""1894. Find the Student that Will Replace the Chalk

tags: array
"""


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)

        i = 0
        while (k := k - chalk[i]) >= 0:
            i += 1

        return i
