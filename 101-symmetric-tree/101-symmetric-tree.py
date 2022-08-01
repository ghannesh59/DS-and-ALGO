# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]
        self.dfs1(root,res1)
        self.dfs2(root,res2)
        if res1==res2:
            return True
        else:
            return False
    def dfs1(self,root,res1):
        if root==None:
            res1.append(None)
            return
        res1.append(root.val)
        self.dfs1(root.left,res1)
        self.dfs1(root.right,res1)
    def dfs2(self,root,res2):
        if root==None:
            res2.append(None)
            return
        res2.append(root.val)
        self.dfs2(root.right,res2)
        self.dfs2(root.left,res2)
        