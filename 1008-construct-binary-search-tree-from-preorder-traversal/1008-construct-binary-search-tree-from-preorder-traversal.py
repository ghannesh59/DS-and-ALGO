# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root=TreeNode(preorder[0])
        stack=[root]
        for i in preorder[1:]:
            if stack[-1].val>i:
                stack[-1].left=TreeNode(i)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val<i:
                    node=stack.pop()
                node.right=TreeNode(i)
                stack.append(node.right)
        return root
                