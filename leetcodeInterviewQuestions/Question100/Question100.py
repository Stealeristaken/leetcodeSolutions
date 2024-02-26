# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_equal(tree1, tree2):
            if tree1 is None and tree2 is None:
                return (True)
            if tree1 is None or tree2 is None:
                return (False)
            check_val = (tree1.val == tree2.val)
            check_left = is_equal(tree1.left, tree2.left)
            check_right = is_equal(tree1.right, tree2.right)
            return (check_val and check_left and check_right)

        return (is_equal(p, q))
    
    
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
