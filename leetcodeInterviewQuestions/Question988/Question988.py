# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def traverse(node: TreeNode, leaf: [str]) -> None:
            nonlocal res
            if node:
                c = chr(ord(chr(node.val)) + ord('a'))
                leaf.append(c)
            if node.left:
                traverse(node.left, leaf)
                leaf.pop()
            if node.right:
                traverse(node.right, leaf)
                leaf.pop()
            if not node.left and not node.right:
                if leaf[::-1] < res[::-1] or not res:
                    res = leaf[:]

        res: [str] = []
        traverse(root, [])
        return ''.join(res[::-1])