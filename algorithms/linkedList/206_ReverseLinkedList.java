/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        /**
         * Iterative solution
         */
        if (head == null || head.next == null) return head;
        
        ListNode left = head.next, curH = head;
        head.next = null;
        while (left != null) {
            ListNode temp = left.next;
            left.next = curH;
            curH = left;
            left = temp;
        }
        return curH;
    }
}

class Solution {
    /**
     * recursive solution
     */
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode nHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return nHead;
    }
}