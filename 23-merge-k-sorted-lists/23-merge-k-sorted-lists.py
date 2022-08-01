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
                heap.append((l.val,l))
        while(len(heap)>0):
            heapq.heapify(heap)
            val,node=heap.pop(0)
            curr.next=ListNode(val)
            curr=curr.next
            node=node.next
            if node:
                heap.append((node.val,node))
        return dummy.next
            
            