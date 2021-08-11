"""1480. Running Sum of 1d Array

difficulty: easy
tags: array
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumsum = nums[:1]
        for v in nums[1:]:
            cumsum.append(v + cumsum[-1])

        return cumsum
