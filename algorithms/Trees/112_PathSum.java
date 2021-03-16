/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        /**
        Don't understand why LeetCode treat an empty tree and target sum 0 as incorrect, if this is not required, then the function can be simplified to two lines
         */
        if (root == null)
            return false;
        
        if (root.left != null && root.right != null)
            return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
        else if (root.left != null)
            return hasPathSum(root.left, sum - root.val);
        else if (root.right != null)
            return hasPathSum(root.right, sum - root.val);
        else
            return sum == root.val;
    }
}