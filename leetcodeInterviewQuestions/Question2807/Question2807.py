# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self._gcd(b, a % b)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next

        while cur:
            tmp = ListNode(self._gcd(prev.val, cur.val))
            prev.next = tmp
            tmp.next = cur

            prev = cur
            cur = cur.next
        
        return head