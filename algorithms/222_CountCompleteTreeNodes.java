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
    public int countNodes(TreeNode root) {
        /**
         * O(logn^2) time with O(logn) space solution
         */
        if (root == null)
            return 0;
        
        int leftH = findH(root.left);
        int rightH = findH(root.right);
        if (leftH == rightH) {
            return (int) Math.pow(2, leftH) + countNodes(root.right);
        } else {
            return (int) Math.pow(2, rightH) + countNodes(root.left);
        }
    }
    
    public int findH(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + findH(root.left);
    }
}