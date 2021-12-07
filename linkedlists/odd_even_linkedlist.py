# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None or head.next.next==None):
            return head
        optr=head
        eptr=head.next
        ehead=head.next
        while(eptr!=None and eptr.next!=None):
            optr.next=optr.next.next
            eptr.next=eptr.next.next
            optr=optr.next
            eptr=eptr.next
        optr.next=ehead
        return head