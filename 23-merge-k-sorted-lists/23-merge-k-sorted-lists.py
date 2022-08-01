# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        dummy=curr=ListNode(0)
        for i in range(len(lists)):
            while(lists[i]!=None):
                res.append(lists[i].val)
                lists[i]=lists[i].next
        res=sorted(res)
        for i in res:
            dummy.next=ListNode(i)
            dummy=dummy.next
        dummy.next=None
        return curr.next
        