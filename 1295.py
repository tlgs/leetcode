"""1295. Find Numbers with Even Number of Digits

difficulty: easy
tags: array
runtime: 99.49
memory: 72.11
"""
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for v in nums:
            cnt += int(math.log10(v)) % 2
        
        return cnt
