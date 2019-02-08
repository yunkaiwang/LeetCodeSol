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
    public void flatten(TreeNode root) {
        /**
        Idea based on inorder traversal, since the flattened tree is actually the inorder traversal
         */
        if (root == null) return;
        Stack<TreeNode> treeNodes = new Stack<TreeNode>();
        
        treeNodes.push(root);
        while (!treeNodes.empty()) {
            root = treeNodes.pop();
            if (root.right != null)
                treeNodes.push(root.right);
            if (root.left != null) {
                root.right = root.left;
                root.left = null;
                treeNodes.push(root.right);
            } else {
                if (!treeNodes.empty())
                    root.right = treeNodes.peek();
            }
        }
    }
}