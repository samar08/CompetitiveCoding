# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        st=""
        p=head
        while(p!=None):
            st+=str(p.val)
            p=p.next
        #print(st)
        out=int(st,2)
        return out