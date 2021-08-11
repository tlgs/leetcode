"""26. Remove Duplicates from Sorted Array

difficulty: easy
tags: array
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]

        return k + 1
