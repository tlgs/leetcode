"""581. Shortest Unsorted Continuous Subarray

This solution makes use of sorting (O(nlogn)) but ends up beating an
O(n) solution that scans the array multiple times because the array in
tests isn't really that big (max 10^4 elements).

difficulty: medium
tags: array
runtime: 76.81
memory: 28.60
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            if snums[left] == nums[left]:
                left += 1

            if snums[right] == nums[right]:
                right -= 1

            if snums[left] != nums[left] and snums[right] != nums[right]:
                return right - left + 1

        return 0
