"""962. Maximum Width Ramp

difficulty: medium
tags: monotonic stack
"""


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, v in enumerate(nums):
            if not stack or v < nums[stack[-1]]:
                stack.append(i)

        m = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                last = stack.pop()
                if i - last > m:
                    m = i - last

        return m
