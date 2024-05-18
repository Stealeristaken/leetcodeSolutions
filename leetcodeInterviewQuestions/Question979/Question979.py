# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def postorder(node):
            if not node:
                return 0
            
            # Recur for left and right subtrees
            left_excess = postorder(node.left)
            right_excess = postorder(node.right)
            
            # Calculate the excess coins of the current node
            current_excess = node.val - 1
            
            # Total moves are the absolute value of the excess coins
            self.moves += abs(left_excess) + abs(right_excess)
            
            # Return the excess coins to the parent node
            return current_excess + left_excess + right_excess
        
        postorder(root)
        return self.moves