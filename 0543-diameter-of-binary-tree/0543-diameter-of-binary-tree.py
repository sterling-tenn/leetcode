# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(node):
            nonlocal longest
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            longest = max(longest, left + right)
            
            return max(left, right) + 1
            
        dfs(root)
        return longest