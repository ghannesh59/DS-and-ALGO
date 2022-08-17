"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        queue=[root]
        while(queue):
            size,temp=len(queue),[]
            for _ in range(size):
                node=queue.pop(0)
                temp.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev=None
            while(temp):
                curr=temp.pop()
                curr.next=prev
                prev=curr
        return root
                