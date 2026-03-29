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

            new = Node(old.val)
            valToNew[old.val] = new
            for old_neighbor in old.neighbors:
                new_neighbor = dfs(old_neighbor)
                new.neighbors.append(new_neighbor)

            return new

        return dfs(node)
