/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        /**
         O(n) solution using constant space
         */
        if (head == null) {
            return head;
        }
        ListNode l = new ListNode(-1);
        l.next = head;
        ListNode cur = l, it = l.next, firstN = null, lastN = null;
        while (it != null) {
            if (it.val < x) {
                if (firstN == null) {
                    it = it.next;
                    cur = cur.next;
                } else {
                    cur.next = it;
                    lastN.next = it.next;
                    it.next = firstN;
                    it = lastN.next;
                    cur = cur.next;
                }
            } else {
                if (firstN == null) {
                    firstN = it;
                }
                lastN = it;
                it = it.next;
            }
        }
        
        return l.next;
    }
}