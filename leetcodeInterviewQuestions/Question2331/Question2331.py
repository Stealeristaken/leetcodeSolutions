class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if root.val == 0 or root.val == 1:
            return bool(root.val)
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)