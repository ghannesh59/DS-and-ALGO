# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=res=ListNode(0)
        p=list1
        q=list2
        while(p and q):
            if p.val>q.val:
                dummy.next=q
                q=q.next
            else:
                dummy.next=p
                p=p.next
            dummy=dummy.next
        while(p or q):
            if p:
                dummy.next=p
                dummy=dummy.next
                p=p.next
            if q:
                dummy.next=q
                dummy=dummy.next
                q=q.next
        dummy.next=None
        return res.next
            
        