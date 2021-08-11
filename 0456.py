"""456. 132 Pattern

We're looking for a subsequence (i, j, k) such that i < k < j.

We start from the end of the list and look for (j, k) pairs.
We use a stack to keep track of the largest valid value for k.
As soon as we find an element that is lesser than our k candidate,
we know we have found an 132 pattern.

difficulty: medium
tags: monotonic stack
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = None

        for v in nums[::-1]:
            if k is not None and v < k:
                return True

            while stack and stack[-1] < v:
                k = stack.pop()

            stack.append(v)

        return False
