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
        
        
        
###########################



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = ListNode(0)
        res.next = head
        slow = fast = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        fast = slow.next
        slow.next = None
        fast = self.reverseTwo(fast)
        slow = res.next
        while fast:
            slowp, fastp = slow.next, fast.next
            slow.next, fast.next = fast, slowp
            slow, fast = slowp, fastp
        return res.next


    def reverseTwo(self, node):
        prev = None
        curr = node
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev