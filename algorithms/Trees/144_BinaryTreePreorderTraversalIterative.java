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
        List<Integer> result = new LinkedList<Integer>();
        
        Stack<TreeNode> l = new Stack<TreeNode>();
        l.push(null);
        while (root != null) {
            result.add(root.val);
            if (root.right != null)
                l.push(root.right);
            if (root.left != null)
                l.push(root.left);
            root = l.pop();
        }
        return result;
    }
}