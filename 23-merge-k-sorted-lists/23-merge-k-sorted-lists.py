# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         res=[]
#         dummy=curr=ListNode(0)
#         for i in range(len(lists)):
#             while(lists[i]!=None):
#                 res.append(lists[i].val)
#                 lists[i]=lists[i].next
#         res=sorted(res)
#         for i in res:
#             dummy.next=ListNode(i)
#             dummy=dummy.next
#         dummy.next=None
#         return curr.next
            if len(lists)==0:
                return None
        
            while(len(lists)>1):
                merged_lists=[]
                for i in range(0,len(lists),2):
                    l1=lists[i]
                    l2=lists[i+1] if (i+1)<len(lists) else None
                    merged_lists.append(self.merge(l1,l2))
                lists=merged_lists
            return lists[0]
    
    def merge(self,l1,l2):
        dummy=curr=ListNode(0)
        while l1 and l2:
            if l1.val>l2.val:
                curr.next=l2
                curr=curr.next
                l2=l2.next
            else:
                curr.next=l1
                curr=curr.next
                l1=l1.next
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dummy.next