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
            return None
        
        copyExists = {}
        
        def get_copy(node) -> Optional['Node']:
            if node in copyExists:
                return copyExists[node]
            
            copy = Node(node.val)
            copyExists[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(get_copy(neighbor))
            
            return copy
        return get_copy(node)