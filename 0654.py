"""654. Maximum Binary Tree

difficulty: medium
tags: monotonic stack, binary tree
runtime: 99.15
memory: 34.45
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        stack = []
        for v in nums:
            node = TreeNode(v, None, None)

            while stack and stack[-1].val < v:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]
