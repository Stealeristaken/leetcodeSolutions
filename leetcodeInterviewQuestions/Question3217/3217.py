                
                
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num=set(nums)
        while head and head.val in num:
            head = head.next
        if not head:
            return None
        current = head
        while current.next:
            if current.next.val in num:
                current.next = current.next.next if current.next.next else None
            else:
                current = current.next
        return head

                
                