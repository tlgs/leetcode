"""496. Next Greater Element I"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for i, v in enumerate(nums2):
            while stack and v > stack[-1]:
                m[stack.pop()] = v
            stack.append(v)

        return [m.get(x, -1) for x in nums1]
