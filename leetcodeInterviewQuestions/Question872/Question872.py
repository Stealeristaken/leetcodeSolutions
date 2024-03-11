# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1,s2=[],[]
        def helper(node,arr):
            if node==None:
                return 0
            if node.left==None and node.right==None:
                arr.append(node.val)
            helper(node.left,arr)
            helper(node.right,arr)
        helper(root1,s1)
        helper(root2,s2)
        return s1==s2