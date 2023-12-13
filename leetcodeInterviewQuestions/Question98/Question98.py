class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        left_valid = self.isValidBST(root.left, min_val, root.val)
        right_valid = self.isValidBST(root.right, root.val, max_val)

        return left_valid and right_valid