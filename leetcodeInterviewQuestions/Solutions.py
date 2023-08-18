'''

    This python file is about regular  leet code questions. I won't write description of questions.
You will see solutions and question names and their numbers.

    !!İf that helped you a bit please drop a star you're welcomed ^^!!

'''

# Question 1 - Two Sum:

class Solution:
    def twoSum(self, nums, target):
        # Create a hash table to store the indices of the elements
        hash_table = {}

        # Iterate through the list of nums
        for i, num in enumerate(nums):
            # Check if target - num is in the hash table
            if target - num in hash_table:
                # If it is, return the indices of the two numbers
                return [hash_table[target - num], i]
            # Otherwise, add the current element and its index to the hash table
            hash_table[num] = i

        # If we reach here, it means we didn't find a solution
        return []

####################################################################################################################################

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