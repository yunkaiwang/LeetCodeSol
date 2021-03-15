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
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null) return new LinkedList<Integer>();
        List<Integer> result = new LinkedList<Integer>();
        result.add(root.val);
        List<Integer> leftChildren = preorderTraversal(root.left);
        List<Integer> rightChildren = preorderTraversal(root.right);
        for (Integer l: leftChildren) {
            result.add(l);
        }
        for (Integer r: rightChildren) {
            result.add(r);
        }
        return result;
    }
}