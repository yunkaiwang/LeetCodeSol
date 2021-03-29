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
    public boolean findTarget(TreeNode root, int k) {
        /**
         * Has to use O(n) space for this question, otherwise we can
         run in O(nlogn) time with O(1) space (find k-num for every
         num in the BST, there are n elements, finding element in BST
         takes O(logn), so total running time is O(nlogn) but the
         space used is constant)
         */
        List<Integer> l = new ArrayList<Integer>();
        inorder(root, l);
        
        int left = 0, right = l.size() - 1;
        while (left < right) {
            int sum = l.get(left) + l.get(right);
            if (sum == k)
                return true;
            if (sum > k)
                right -= 1;
            else
                left += 1;
        }
        return false;
    }
    
    public void inorder(TreeNode root, List<Integer> list) {
        if (root == null) return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}