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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> paths = new LinkedList<List<Integer>>();
        pathSumHelper(root, sum, paths, null);
        return paths;
    }
    
    public void pathSumHelper(TreeNode root, int sum, List<List<Integer>> paths, List<Integer> currentPath) {
        if (root == null) return;
        
        if (currentPath == null)
            currentPath = new LinkedList<Integer>();
        currentPath.add(root.val);
        sum -= root.val;
        if (root.left != null && root.right != null) {
            pathSumHelper(root.left, sum, paths, currentPath);
            pathSumHelper(root.right, sum, paths, currentPath);
        } else if (root.left != null) {
            pathSumHelper(root.left, sum, paths, currentPath);
        } else if (root.right != null) {
            pathSumHelper(root.right, sum, paths, currentPath);
        } else {
            if (sum == 0)
                paths.add(new LinkedList<Integer>(currentPath));
        }
        currentPath.remove(currentPath.size() - 1);   
    }
}