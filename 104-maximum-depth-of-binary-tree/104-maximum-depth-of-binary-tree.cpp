/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0; // Base case
        
        // Find depths of left and right subtrees
        int maxLeft = maxDepth(root->left);
        int maxRight = maxDepth(root->right);
        
        return std::max(maxLeft,maxRight) + 1; // Add 1 because a single node has a depth of 1
    }
};