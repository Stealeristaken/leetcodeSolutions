# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        prev = head
        sum = 0

        while current.next:
            while current.val != 0:
                sum = sum + current.val
                current = current.next
            prev.val = sum

            if current.next:
                prev.next = current
                prev = current
                current = current.next
                sum = 0

        prev.next = None

        return head