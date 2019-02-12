/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        ListNode currA = headA, currB = headB;
        ListNode lastA = null, lastB = null;
        
        while (currA != currB) {
            if (lastA != null && lastB != null && lastA != lastB)
                return null;
            
            if (currA.next != null) {
                currA = currA.next;
            } else {
                if (lastA == null)
                    lastA = currA;
                currA = headB;
            }
            
            if (currB.next != null) {
                currB = currB.next;
            } else {
                if (lastB == null)
                    lastB = currB;
                currB = headA;
            }
        }
        return currA;
    }
}