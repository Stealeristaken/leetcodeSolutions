from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int: 
        if root == None:
            return 0
        if root.left != None and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
  
  
  
#################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        stack = [(root, 0)]
        while stack:
            root, pos = stack.pop()
            if pos and not root.left and not root.right:
                total += root.val
            if root.left:
                stack.append((root.left, 1))
            if root.right:
                stack.append((root.right, 0))

        return total