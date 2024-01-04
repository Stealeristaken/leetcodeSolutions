class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print(f"preorder: {preorder}  inorder: {inorder}")
        if inorder:
            root = TreeNode(preorder[0])
            root_inorder = inorder.index(preorder[0])

            root.left = self.buildTree(preorder[1:1 + root_inorder], inorder[:root_inorder])
            root.right = self.buildTree(preorder[root_inorder + 1:], inorder[root_inorder + 1:])

            return root
