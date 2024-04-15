from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, num):
            if not node:
                return 0
            num = num * 10 + node.val
            if not node.left and not node.right:
                return num
            return dfs(node.left, num) + dfs(node.right, num)
        
        return dfs(root, 0)
  
  
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        sum_root_to_leaf_numbers = 0
        def preorder(node, curr_sum):
            if not node: return 0

            nonlocal sum_root_to_leaf_numbers
            curr_sum = curr_sum * 10 + node.val

            if not(node.left or node.right):
                sum_root_to_leaf_numbers += curr_sum
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
        
        preorder(root, 0)
        return sum_root_to_leaf_numbers