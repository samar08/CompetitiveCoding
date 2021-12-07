/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null)return head;

        ListNode head1 = head, head2 = head.next;
        ListNode tail1 = head1, tail2 = head2;

        while(tail2 != null && tail1 != null){
            tail1.next = tail2.next;
            if(tail1.next == null)break;
            tail1 = tail1.next;

            if(tail1 != null){
                tail2.next = tail1.next;
                tail2 = tail2.next;
            }
        }

        tail1.next = head2;
        return head1;
    }
}