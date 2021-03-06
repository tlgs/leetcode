"""496. Next Greater Element I

difficulty: easy
tags: monotonic stack, hash table
runtime: 87.75
memory: 71.31
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for _, v in enumerate(nums2):
            while stack and stack[-1] < v:
                m[stack.pop()] = v

            stack.append(v)

        return [m.get(x, -1) for x in nums1]
