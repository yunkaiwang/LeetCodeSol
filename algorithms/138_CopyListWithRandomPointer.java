/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return head;
        
        RandomListNode curr = head, copy;
        while (curr != null) {
            copy = new RandomListNode(curr.label);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }
        
        curr = head;
        while (curr != null) {
            if (curr.random != null)
                curr.next.random = curr.random.next;
            curr = curr.next.next;
        }
        RandomListNode new_head = head.next, curr_copy_node = head.next;
        curr = head;
        while (curr != null) {
            curr.next = curr_copy_node.next;
            if (curr_copy_node.next != null)
                curr_copy_node.next = curr_copy_node.next.next;
            curr = curr.next;
            curr_copy_node = curr_copy_node.next;
        }
        
        return new_head;
    }
}