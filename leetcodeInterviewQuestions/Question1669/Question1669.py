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