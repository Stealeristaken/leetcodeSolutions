class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail=list1
        for _ in range (a-1):
            tail=tail.next
        head = tail # the last node of the first part of list1 
        for _ in range (b-a+2):
            tail=tail.next
		# tail - the first node of the second part of list2 
        head.next=list2
        while head.next:
            head=head.next
		# head - the last node of list2	
        head.next=tail
        return list1              
  
  
  
################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def getTail(tail):
            while tail and tail.next:
                tail = tail.next
            return tail

        def getNodesAtIndex(head, k1, k2):
            first = second = head
            for i in range(k2):
                if i == k1: first = second
                second = second.next
            return first, second
        
        node1, node2 = getNodesAtIndex(list1, a - 1, b)
        list2Tail = getTail(list2)
        node1.next, list2Tail.next = list2, node2.next

        return list1