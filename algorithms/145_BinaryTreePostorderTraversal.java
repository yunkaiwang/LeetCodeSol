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
        List<Integer> res = new LinkedList<Integer>();
        
        return postorderTraversalRec(root, res);
    }
    
    public List<Integer> postorderTraversalRec(TreeNode root, List<Integer> cur) {
        if (root == null) return cur;
        postorderTraversalRec(root.left, cur);
        postorderTraversalRec(root.right, cur);
        cur.add(root.val);
        return cur;
    }
}