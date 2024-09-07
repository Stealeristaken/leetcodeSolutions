class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, node):
            # Base case: If we have reached the end of the linked list
            if head is None:
                return True
            # Base case: If we have reached a leaf node or the current node value does not match
            if node is None or head.val != node.val:
                return False
            # Continue the search in left and right subtrees
            return dfs(head.next, node.left) or dfs(head.next, node.right)

        def search_tree(node):
            if node is None:
                return False
            # Check if the linked list can be found starting from the current node
            if dfs(head, node):
                return True
            # Continue the search in left and right subtrees
            return search_tree(node.left) or search_tree(node.right)

        return search_tree(root)