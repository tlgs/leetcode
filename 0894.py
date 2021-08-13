"""894. All Possible Full Binary Trees

difficulty: medium
tags: dynamic programming, binary tree
runtime: 96.50
memory: 94.51
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mem = {1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n not in self.mem:
            self.mem[n] = [
                TreeNode(0, left, right)
                for i in range(1, n, 2)
                for left in self.allPossibleFBT(i)
                for right in self.allPossibleFBT(n - 1 - i)
            ]

        return self.mem[n]
