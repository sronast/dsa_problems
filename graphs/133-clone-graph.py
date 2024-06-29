"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        lookup = {}

        def dfs(node):
            if node in lookup:
                return
            lookup[node] =(Node(node.val), [])
            for neigh in node.neighbors:
                lookup[node][1].append(neigh)
                dfs(neigh)

        dfs(node)

        for k, v in lookup.items():
            for val in v[1]:
                v[0].neighbors.append(lookup[val][0])
        return lookup[node][0]
        