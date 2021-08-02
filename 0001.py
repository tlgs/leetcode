"""1. Two Sum"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            j = seen.get(target - v)
            if j is not None:
                return [j, i]
            seen[v] = i
        
        return []
