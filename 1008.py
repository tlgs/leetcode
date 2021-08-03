"""1008. Construct Binary Search Tree from Preorder Traversal"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0], None, None)

        stack = [root]
        for v in preorder[1:]:
            node = TreeNode(v, None, None)

            if v < stack[-1].val:
                stack[-1].left = node

            else:
                while stack and v > stack[-1].val:
                    last = stack.pop()
                last.right = node

            stack.append(node)

        return root
