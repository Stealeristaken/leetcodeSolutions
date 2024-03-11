# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # First, every Node in left or right subtree from current Node,
        #  can be considered as descendant. And every Node above is ancestor.
        # To get maximised difference, we need to find minimum and maximum of current Node subtrees.
        # Because we can have Node.val == 5, and in subtrees min == 0 and max == 100.
        # So, we will get maximum difference with abs(5 - 100).
        # Or, if we think about it more and don't rush as I did, we can just take:
        #  ! maximum of subtree - minimum of subtree == maximum difference !
        # But w.e., not so slow and working.

        def dfs(node: TreeNode) -> tuple[int, int, int]:
            # If no childs.
            # `node.val` is maximum and minimum values we can have in this subtree.
            min_value: int = node.val
            max_value: int = node.val
            # Minimum diff we can have == 0.
            cur_max_diff: int = 0
            max_diff: int = 0
            if node.left:
                min_val_in_left, max_val_in_left, max_so_far = dfs(node.left)
                cur_max_diff = max(
                    abs(node.val - min_val_in_left),
                    abs(node.val - max_val_in_left),
                )
                min_value = min(min_val_in_left, min_value)
                max_value = max(max_val_in_left, max_value)
                max_diff = max(max_so_far, cur_max_diff)
            if node.right:
                min_val_in_right, max_val_in_right, max_so_far = dfs(node.right)
                cur_max_diff = max(
                    abs(node.val - min_val_in_right),
                    abs(node.val - max_val_in_right),
                    cur_max_diff,
                )
                min_value = min(min_val_in_right, min_value)
                max_value = max(max_val_in_right, max_value)
                max_diff = max(max_so_far, cur_max_diff, max_diff)
            # (minimum value in current subtree, maximum value in current subtree, max_difference we found so far)
            return min_value, max_value, max_diff

        return dfs(root)[2]