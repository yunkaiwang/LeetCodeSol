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
    public TreeNode sortedArrayToBST(int[] nums) {
        /**
        O(n) solution
         */
        if (nums.length == 0) return null;
        return sortedArrayToBST(nums, 0, nums.length - 1);
    }
    
    public TreeNode sortedArrayToBST(int[] nums, int left, int right) {
        if (left > right) return null;
        int middle = (int) (right - left)/2 + left;
        TreeNode root = new TreeNode(nums[middle]);
        root.left = sortedArrayToBST(nums, left, middle - 1);
        root.right = sortedArrayToBST(nums, middle + 1, right);
        return root;
    }
}