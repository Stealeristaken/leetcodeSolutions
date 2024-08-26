from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = list()
        def helper(root):
            if root:
                for child in root.children:
                    helper(child)
                out.append(root.val)
        helper(root)
        return out