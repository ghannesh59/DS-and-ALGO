# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[]
        curr=dummy=ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(heap,(l.val,l))
        while(len(heap)>0):
            val,node=heapq.heappop(heap)
            curr.next=ListNode(val)
            curr=curr.next
            node=node.next
            if node:
                heapq.heappush(heap,(node.val,node))
        return dummy.next
            
            