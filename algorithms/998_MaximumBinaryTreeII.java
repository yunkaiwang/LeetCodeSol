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
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        TreeNode node = new TreeNode(val);
        if (root == null || val > root.val) {
            node.left = root;
            return node;
        }
        
        TreeNode curr = root;
        while (curr.right != null) {
            if (val > curr.right.val) {
                node.left = curr.right;
                curr.right = node;
                return root;
            }
            curr = curr.right;
        }
        curr.right = node;
        return root;
    }
}