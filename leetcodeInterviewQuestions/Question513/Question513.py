# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans=[]
        q=deque([root])
        while q:
            n=len(q)
            arr=[]
            for i in range(n):
                curr=q.popleft()
                arr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if arr:
                ans.append(arr)

        return ans[-1][0]
  
  
  
  
##############


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = [0] * 2

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.res[1]

    def dfs(self, node, depth):
        if not node:
            return

        if depth > self.res[0]:
            self.res[0] = depth
            self.res[1] = node.val
        
        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)
    


        