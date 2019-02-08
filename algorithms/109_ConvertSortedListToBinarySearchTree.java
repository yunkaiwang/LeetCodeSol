/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        /**
        O(n) solution by converting list into array
         */
        int size = 0;
        ListNode cur = head;
        while (cur != null) {
            size += 1;
            cur = cur.next;
        }
        cur = head;
        int[] nums = new int[size];
        for (int i = 0; i < size; ++i) {
            nums[i] = cur.val;
            cur = cur.next;
        }
        
        return sortedArrayToBST(nums);
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
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
}

class Solution {
    ListNode cur = null;
    
    public TreeNode sortedListToBST(ListNode head) {
        /**
        Another O(n) solution but this one runs much faster than previous one
         */
        int size = 0;
        cur = head;
        while (cur != null) {
            size += 1;
            cur = cur.next;
        }
        cur = head;
        return sortedArrayToBST(0, size-1);
    }
    
    public TreeNode sortedArrayToBST(int start, int end) {
        if (start > end) return null;
        
        int middle = (int) (end - start)/2 + start;
        TreeNode left = sortedArrayToBST(start, middle - 1);
        
        TreeNode root = new TreeNode(cur.val);
        cur = cur.next;
        root.left = left;
        root.right = sortedArrayToBST(middle + 1, end);
        
        return root;
    }
}