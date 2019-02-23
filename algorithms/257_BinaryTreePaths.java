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
    public List<String> binaryTreePaths(TreeNode root) {
        /**
         * linear time solution
         */
        List<String> paths = new LinkedList<String>();
        
        if (root == null)
            return paths;
        String currentPath = Integer.toString(root.val);
        this.pathHelper(root, currentPath, paths);
        
        return paths;
    }
    
    public void pathHelper(TreeNode root, String currentPath, List<String> paths) {
        if (root.left == null && root.right == null) {
            paths.add(currentPath);
        } else {
            if (root.left != null)
                this.pathHelper(root.left, currentPath + "->" + Integer.toString(root.left.val), paths);
                
            if (root.right != null)
                this.pathHelper(root.right, currentPath + "->" + Integer.toString(root.right.val), paths);
        }
    }
}