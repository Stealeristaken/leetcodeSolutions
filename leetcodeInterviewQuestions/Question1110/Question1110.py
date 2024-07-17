# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ReverseNode:
    def __init__(self, this, parent=None, dir=None):
        self.this = this
        self.parent = parent
        self.dir = dir

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        lookup = {} # Dict[int, ReverseNode]

        def traverse(n: TreeNode, parent: Optional[ReverseNode] = None, dir: Optional[str] = None) -> None:
            if not n:
                return
            
            lookup[n.val] = ReverseNode(n, parent, dir)
            traverse(n.left, n, "L")
            traverse(n.right, n, "R")

        traverse(root)

        forest = set([root])
        for td in to_delete:
            rn = lookup[td]
            
            if rn.this in forest:
                forest.remove(rn.this)
            
            if rn.this.left:
                forest.add(rn.this.left)
            if rn.this.right:
                forest.add(rn.this.right)

            if not rn.parent:
                continue
            
            p = rn.parent
            # Parent disown child
            if rn.dir == "L":
                p.left = None
            elif rn.dir == "R":
                p.right = None
        
        return list(forest)
            