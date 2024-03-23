# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,node):
        curr=node
        prev=None
        while(curr):
            if(not curr.next):
                curr.next=prev
                return curr
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
    
    def mergeList(self,l1,l2):
        while(l2):
            n1=l1.next
            n2=l2.next
            l1.next=l2
            l2.next=n1
            l1=n1
            l2=n2

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        nh=slow.next
        slow.next=None
        reversedHead=self.reverseList(nh)
        self.mergeList(head,reversedHead)