"""1909. Remove One Element to Make the Array Strictly Increasing (EASY)

tags: array
"""


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        deleted = False
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                if deleted:
                    return False

                deleted = True
                if i > 1 and nums[i] <= nums[i - 2]:
                    continue

            prev = nums[i]

        return True
