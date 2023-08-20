#Question 2 - Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to store the result
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Iterate until both linked lists are not empty
        while l1 or l2:
            # Get the values of the current nodes in the linked lists
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and the carry
            sum = x + y + carry
            carry = sum // 10
            sum %= 10

            # Create a new node with the sum as its value
            current.next = ListNode(sum)
            current = current.next

            # Move to the next nodes in the linked lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there is a carry left, add it to the result
        if carry:
            current.next = ListNode(carry)

        # Return the result without the dummy node
        return dummy.next
