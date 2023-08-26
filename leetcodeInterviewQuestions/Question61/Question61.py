# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
The problem requires rotating a linked list to the right by k positions.
To solve this, we need to find the length of the linked list, adjust k to handle rotations that exceed the length, and then perform the rotation by adjusting the pointers of the linked list nodes.

Approach
First, we handle the edge cases:
if the linked list is empty or has only one node, there's no need to rotate, so we return the original head.
We find the length of the linked list and also keep track of the tail node.
We adjust k to be k % length to handle rotations that are greater than the length of the linked list.
If k becomes 0 after adjusting, it means the list is rotated back to its original position, so we return the original head.
We then find the new head of the rotated list by traversing to the (length - k - 1)-th node.
Adjust the pointers to rotate the list: set the tail node's next pointer to the original head, and update the next pointer of the (length - k - 1)-th node to None.
Return the new head, which is the (length - k)-th node after rotation.
'''


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if k == 0:
            return head

        current = head
        for i in range(length - k - 1):
            current = current.next

        newHead = current.next
        tail.next = head
        current.next = None
        return newHead