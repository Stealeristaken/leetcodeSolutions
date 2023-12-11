# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.helper(root, output)
        return output

    def helper(self, root, output):
        if root:
            self.helper(root.left, output)
            output.append(root.val)
            self.helper(root.right, output)

