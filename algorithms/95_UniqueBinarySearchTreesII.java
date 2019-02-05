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
    public List<TreeNode> generateTrees(int n) {
        if (n==0) { return new LinkedList<TreeNode>(); }
        int[] arr = new int[n];
        for (int i=0; i<n; ++i) {
            arr[i] = i+1;
        }
        return dfs(arr);
    }
    
    public List<TreeNode> dfs(int[] remaining) {
        List<TreeNode> trees = new LinkedList<TreeNode>();
        if (remaining.length == 0) {
            trees.add(null);
            return trees;
        }
        
        for (int i=0; i< remaining.length; ++i) {
            List<TreeNode> leftChilds = dfs(Arrays.copyOfRange(remaining, 0, i));
            List<TreeNode> rightChilds = dfs(Arrays.copyOfRange(remaining, i+1, remaining.length));
            for (TreeNode l: leftChilds) {
                for (TreeNode r: rightChilds) {
                    TreeNode root = new TreeNode(remaining[i]);
                    root.left = l;
                    root.right = r;
                    trees.add(root);
                }
            }
        }
        return trees;
    }
}