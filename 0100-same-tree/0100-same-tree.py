# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # None cases
        if not p and not q: # both None
            return True
        if p is None or q is None: # xor = different
            return False
        
        # value case
        if p.val != q.val:
            return False
        
        # are the lefts/rights of each tree the same
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        # both must be the same
        return left and right