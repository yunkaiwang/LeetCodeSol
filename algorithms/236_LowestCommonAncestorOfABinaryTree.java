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
    boolean visitedP = false;
    boolean visitedQ = false;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        /**
         * solution based on post order traversal
         */
        return postOrderHelper(root, p, q);
    }
    
    public TreeNode postOrderHelper(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null)
            return null;
        
        TreeNode temp = postOrderHelper(root.left, p, q);
        if (temp != null) return temp;
        boolean oldP = visitedP, oldQ = visitedQ;
        visitedP = visitedQ = false;
        temp = postOrderHelper(root.right, p, q);
        if (temp != null) return temp;
        visitedP |= oldP;
        visitedQ |= oldQ;
        if (root == p) visitedP = true;
        if (root == q) visitedQ = true;
        if (visitedP && visitedQ)
            return root;
        return null;
    }
}