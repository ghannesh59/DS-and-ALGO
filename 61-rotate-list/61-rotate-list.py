# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        count=1
        curr=head
        while(curr.next):
            curr=curr.next
            count=count+1
        k=k%count
        curr.next=head
        temp=head
        for i in range(count-k-1):
            temp=temp.next
        answer=temp.next
        temp.next=None
        return answer
        
            
            