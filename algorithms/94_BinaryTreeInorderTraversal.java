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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<Integer>();
        if (root == null) { return res; }
        
        List<Integer> temp = inorderTraversal(root.left);
        for (Integer i: temp) {
            res.add(i);
        }
        res.add(root.val);
        temp = inorderTraversal(root.right);
        for (Integer i: temp) {
            res.add(i);
        }
        return res;
    }
}