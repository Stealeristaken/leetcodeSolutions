# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp = head
        ans = []
        while temp:
            ans.append(temp.val)
            temp = temp.next

        def convertToBST(left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(ans[left])
            mid = (left + right) // 2
            root = TreeNode(ans[mid])
            root.left = convertToBST(left, mid - 1)
            root.right = convertToBST(mid + 1, right)
            return root

        return convertToBST(0, len(ans) - 1)