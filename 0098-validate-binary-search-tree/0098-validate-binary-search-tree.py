# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validate(root, float('-inf'), float('inf'))
    
    def validate(self, node: Optional[TreeNode], low: int, high: int) -> bool:
            # base case, empty
            if not node:
                return True
            
            # is valid value?
            if not (low < node.val < high):
                return False
            
            leftValid = self.validate(node.left, low, node.val) # max of left subtree is current val
            rightValid = self.validate(node.right, node.val, high) # min of right subtree is current val
            
            return leftValid and rightValid