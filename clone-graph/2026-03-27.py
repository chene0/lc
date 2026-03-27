"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        valToNew = {}

        def dfs(old):
            if old.val in valToNew:
                return valToNew[old.val]

            valToNew[old.val] = Node(old.val)
            for old_neighbor in old.neighbors:
                new_neighbor = dfs(old_neighbor)
                valToNew[old.val].neighbors.append(new_neighbor)

            return valToNew[old.val]

        return dfs(node)
