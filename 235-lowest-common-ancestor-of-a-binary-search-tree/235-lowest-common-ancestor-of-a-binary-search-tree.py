# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        if curr.val>p.val and curr.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif curr.val<p.val and curr.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        
        