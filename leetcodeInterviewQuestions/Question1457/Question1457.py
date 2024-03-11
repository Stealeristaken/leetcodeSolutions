# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def count(node: TreeNode, unpaired: int, isOdd: bool) -> int:
            """
            Counts number of root-to-leaf paths, from node downward,
            whose values are palindromic
            """

            new_unpaired = unpaired ^ (1 << node.val)
            if node.left or node.right:
                ans = 0
                if node.left:
                    ans += count(node.left, new_unpaired, not isOdd)
                if node.right:
                    ans += count(node.right, new_unpaired, not isOdd)
                return ans
            else:
                if isOdd:
                    return int(int.bit_count(new_unpaired) == 1)
                else:
                    return int(int.bit_count(new_unpaired) == 0)

        return count(root, 0, True)