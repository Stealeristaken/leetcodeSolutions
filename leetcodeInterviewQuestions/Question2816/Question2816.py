# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        p, carry = head, 0
        while p:
            tail = p
            p.val, carry = (p.val * 2 + carry) % 10, p.val // 5
            p = p.next
        if carry:
            tail.next = ListNode(carry)
        return self.reverseList(head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, q = None, head
        while q:
            x, q.next = q.next, p
            p, q = q, x
        return p