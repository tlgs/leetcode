"""684. Redundant Connection

This is a rather barebones union-find solution;
No path compression or union-by-size/rank.

difficulty: medium
tags: union-find
runtime: 96.31
memory: 87.37
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [v for v in range(len(edges) + 1)]

        def find(x):
            return x if parent[x] == x else find(parent[x])

        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return False

            parent[y] = x
            return True

        last = None
        for edge in edges:
            if not union(*edge):
                last = edge

        return last
