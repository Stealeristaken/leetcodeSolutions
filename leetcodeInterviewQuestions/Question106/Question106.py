# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper={}
        for i, j in enumerate(inorder):
            mapper[j]=i

        def rec(low,high):
            if low>high:
                return
            root=TreeNode(postorder.pop())
            mid=mapper[root.val]
            root.right=rec(mid+1, high)
            root.left=rec(low, mid-1)
            return root

        return rec(0,  len(inorder)-1)