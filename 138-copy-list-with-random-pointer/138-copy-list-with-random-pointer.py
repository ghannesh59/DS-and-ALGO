"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        org_to_clone={None:None}
        while(curr):
            copy=Node(curr.val)
            org_to_clone[curr]=copy
            curr=curr.next
        curr=head
        while(curr):
            copy=org_to_clone[curr]
            copy.next=org_to_clone[curr.next]
            copy.random=org_to_clone[curr.random]
            curr=curr.next
        return org_to_clone[head]
            