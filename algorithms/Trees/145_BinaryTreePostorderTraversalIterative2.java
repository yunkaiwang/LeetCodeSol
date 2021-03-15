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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while (root != null || !stack.empty()) {
            while (root != null) {
                if (root.right != null)
                    stack.push(root.right);
                stack.push(root);
                root = root.left;
            }
            
            root = stack.pop();
            if (root.right != null && !stack.empty() && root.right == stack.peek()) {
                stack.pop();
                stack.push(root);
                root = root.right;
            } else {
                result.add(root.val);
                root = null;
            }
        }
        return result;
    }
}