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
    /**
     * worst case O(n) run time guaranteed solution
     */
    private int ans;
    private int count;
    
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        helper(root);
        return ans;
    }
    
    public void helper(TreeNode root) {
        if (root == null)
            return;
        helper(root.left);
        --count;
        if (count == 0) {
            ans = root.val;
            return;
        }
            
        helper(root.right);
    }
}

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        /**
         * O(n) on average runtime, O(n^2) worst case run time
         */
        int leftCount = countTree(root.left);
        if (k <= leftCount)
            return kthSmallest(root.left, k);
        else if (k == leftCount + 1)
            return root.val;
        else
            return kthSmallest(root.right, k-leftCount-1);
    }
    
    public int countTree(TreeNode root) {
        if (root == null)
            return 0;
        return 1 + countTree(root.left) + countTree(root.right);
    }
}