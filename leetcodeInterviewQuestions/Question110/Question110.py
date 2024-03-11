# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_balanced=True

        def traverse(root):
            nonlocal height_balanced
            if not root:
                return 0
            left_subtree_height=traverse(root.left)
            right_subtree_height=traverse(root.right)
            if abs(left_subtree_height-right_subtree_height)>1:
                height_balanced=False
            return max(left_subtree_height, right_subtree_height)+1
        traverse(root)
        return height_balanced