# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        self.dfs(root,res)
        print(res)
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True
    def dfs(self,root,res):
        if root ==None:
            return
        self.dfs(root.left,res)
        res.append(root.val)
        self.dfs(root.right,res)
        