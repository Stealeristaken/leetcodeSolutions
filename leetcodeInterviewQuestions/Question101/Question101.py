class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left = root.left
        right = root.right
        lstack = []
        rstack = []
        while True:
            if (not left or not right) or left.val != right.val:
                return False
            if left.right and right.left:
                    lstack.append(left.right)
                    rstack.append(right.left)
            elif left.right or right.left:
                return False
            if left.left and right.right:
                    left = left.left
                    right = right.right
            elif left.left or right.right:
                    return False
            elif len(lstack) != 0 and len(rstack) != 0:
                    left = lstack.pop()
                    right = rstack.pop()
            elif len(lstack) == 0 and len(rstack) == 0:
                    return True
            else:
                return False