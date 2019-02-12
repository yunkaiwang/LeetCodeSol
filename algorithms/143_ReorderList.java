/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode fast = head.next, slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        ListNode secondHalfHead = slow.next;
        ListNode curr = secondHalfHead.next, temp;
        secondHalfHead.next = null;
        slow.next = null;
        while (curr != null) {
            temp = curr.next;
            curr.next = secondHalfHead;
            secondHalfHead = curr;
            curr = temp;
        }
        
        ListNode first = head;
        ListNode second = secondHalfHead;
        while (second != null) {
            temp = first.next;
            first.next = second;
            second = second.next;
            
            first.next.next = temp;
            first = temp;
        }
    }
}