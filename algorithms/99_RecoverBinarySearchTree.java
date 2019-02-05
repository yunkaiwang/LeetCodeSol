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
    TreeNode firstE = null;
    TreeNode secondE = null;
    TreeNode prev = new TreeNode(Integer.MIN_VALUE);
    public void recoverTree(TreeNode root) {
        inorder(root);
        if (firstE == null || secondE == null)
            return;
        firstE.val = secondE.val + firstE.val;
        secondE.val = firstE.val - secondE.val;
        firstE.val = firstE.val - secondE.val;
    }
    
    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        if (root.val <= prev.val) {
            if (firstE == null)
                firstE = prev;
            secondE = root;
        }
        prev = root;
        inorder(root.right);
    }
}