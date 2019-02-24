/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        /**
         * O(n) time with O(1) space, but the input list is modified
         */
        ListNode fast = head, slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        if (fast != null)
            slow = slow.next;
        
        slow = reverse(slow);
        fast = head;
        while (slow != null) {
            if (slow.val != fast.val)
                return false;
            slow = slow.next;
            fast = fast.next;
        }
        return true;
    }
    
    public ListNode reverse(ListNode head) {
        ListNode prev = null, temp = null;
        while (head != null) {
            temp  = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }


    public boolean isPalindrome(ListNode head) {
        /**
         * O(n) time and O(n) space
         */
        List<Integer> l = new ArrayList<Integer>();
        ListNode cur = head;
        while (cur != null) {
            l.add(cur.val);
            cur = cur.next;
        }
        int left = 0, right = l.size() - 1;
        while (left < right) {
            if (!l.get(left).equals(l.get(right)))
                return false;
            ++left;
            --right;
        }
        return true;
    }
}