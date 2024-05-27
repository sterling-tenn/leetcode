# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        
        # recursively:
        # inorder:   left -> root (INDEX i HERE) -> right
        # postorder: left -> right       "       -> root
        root = TreeNode(postorder[-1]) # root node is always the last of postorder
        i = inorder.index(postorder[-1]) # where is the index of the root node in the inorder list
        
        # splitting using index i, we can easily see which items are left and right
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1]) # sizes must be the same, and we must still pass the last node of postorder is passed recursively
        
        return root