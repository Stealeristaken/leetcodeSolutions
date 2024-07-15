# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        child = set()
        for p, c, l in descriptions:
            child.add(c)
            if p in d:
                p = d[p]
            else:
                d[p] = TreeNode(p)
                p = d[p]
            if c in d:
                c = d[c]
            else:
                d[c] = TreeNode(c)
                c = d[c]
            if l:
                p.left = c
            else:
                p.right = c

        for p, _, _ in descriptions:
            if p not in child: return d[p]
        
        return None