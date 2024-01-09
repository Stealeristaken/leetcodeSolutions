# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node is None:
                return 0
            leftCount = traverse(node.left)
            rightCount = traverse(node.right)
            if leftCount == 0 and node.left is None and node.right is not None:
                return 1 + rightCount
            if rightCount == 0 and node.right is None and node.left is not None:
                return 1 + leftCount
            return 1 + min(leftCount, rightCount)
        return traverse(root)