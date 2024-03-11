class Solution:
      def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
          def height(root):
              if root is None:
                  return 0
              left = height(root.left)
              right = height(root.right)
              self.ans = max(self.ans,left+right)
              return 1+max(left,right)
          self.ans = 0
          height(root)
          return self.ans
    
    
    
    
#############################################

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left) 
            right = dfs(node.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
        