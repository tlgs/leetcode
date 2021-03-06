"""1. Two Sum

difficulty: easy
tags: hash table, array
runtime: 73.03
memory: 20.73
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            j = seen.get(target - v)
            if j is not None:
                return [j, i]
            seen[v] = i

        return []
