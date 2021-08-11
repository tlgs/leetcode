"""1019. Next Greater Node In Linked List

difficulty: medium
tags: monotonic stack, linked list
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        ans = [0] * len(nums)
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                ans[stack.pop()] = v

            stack.append(i)

        return ans
