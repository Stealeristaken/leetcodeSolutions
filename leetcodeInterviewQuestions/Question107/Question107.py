# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_mapper, q, output, max_level = {}, deque(), [], 0
        if not root:
            return output

        q.append((0, root))
        while q:
            level, node = q.popleft()
            if level not in level_mapper:
                level_mapper[level] = []
            if level > max_level:
                max_level = level

            level_mapper[level].append(node.val)

            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        for i in reversed(range(max_level + 1)):
            output.append(level_mapper[i])

        return output