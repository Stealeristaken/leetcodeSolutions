from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(node, d):
            if not node: return
            if d == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        dfs(root, 1)
        return root