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
  
  
  
  
  
#######################


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def doubleIt(self, head):
        curr = head 
        if curr.val > 4: 
            head = ListNode(1, head) 
            # ans = ListNode(1, head)
        while curr.next: 
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next 
        curr.val = (curr.val * 2) % 10

        return head