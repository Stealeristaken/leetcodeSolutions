class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        path = []
        def dfs(nd: Optional[TreeNode], ts: int):
            path.append(nd.val)
            if not (nd.left or nd.right) and nd.val == ts:
                res.append(path[:])
                path.pop()
                return

            if nd.left:
                dfs(nd.left, ts-nd.val)
            if nd.right:
                dfs(nd.right, ts-nd.val)
            path.pop()

        dfs(root, targetSum)
        return res