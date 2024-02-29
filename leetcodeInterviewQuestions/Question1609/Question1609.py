class Solution:
      def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
          q = deque([root])
          level = 0
          while q:
              prev = None
              n = len(q)
              for i in range(n):
                  node = q.popleft()
                  if level % 2 == 0:
                      if node.val % 2 == 0 or (prev and prev >= node.val):
                          return False
                  else:
                      if node.val % 2 != 0 or (prev and prev <= node.val):
                          return False
                  prev = node.val
                  if node.left:
                      q.append(node.left)
                  if node.right:
                      q.append(node.right)
              level += 1
          return True
    
    
    
    
####################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        is_odd = False
        while q:
            new_q = []
            prev = None
            for node in q:
                if is_odd:
                    if node.val % 2 or (prev and prev.val <= node.val):
                        return False
                else:
                    if not node.val % 2 or (prev and prev.val >= node.val):
                        return False
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                prev = node
            q = new_q
            is_odd = not is_odd
        return True