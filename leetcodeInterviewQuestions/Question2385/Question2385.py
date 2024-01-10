# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, d):
        if root == None:
            return
        if (root.left):
            d[root.val].append(root.left.val)
            d[root.left.val].append(root.val)
            self.solve(root.left, d)
        if (root.right):
            d[root.val].append(root.right.val)
            d[root.right.val].append(root.val)
            self.solve(root.right, d)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d = defaultdict(list)
        self.solve(root, d)
        visited = set()
        queue = [start]
        ans = -1
        while queue:
            queue2 = queue.copy()
            queue = []
            print(queue2)
            while queue2:
                val = queue2.pop()
                if (val in visited):
                    continue
                visited.add(val)
                for i in d[val]:
                    if (i in visited):
                        continue
                    else:
                        queue += [i]
            ans += 1
        return ans

