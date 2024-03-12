# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        seen,total = {},0

        while temp:
            total+=temp.val

            if total in seen:
                prev = seen[total]
                temp = prev.next
                currTotal = total+temp.val
                while currTotal !=total:
                    del seen[currTotal]
                    temp = temp.next
                    currTotal+=temp.val
                prev.next = temp.next
            else:
                seen[total] = temp

            temp=temp.next

        return dummy.next
  
  
  
##########################################

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sums = {0: front}
        # Calculate the prefix sum for each node and add to the hashmap
        # Duplicate prefix sum values will be replaced
        while current:
            prefix_sum += current.val
            prefix_sums[prefix_sum] = current
            current = current.next
        # Reset prefix sum and current
        prefix_sum = 0
        current = front
        # Delete zero sum consecutive sequences by setting node before sequence to node after
        while current:
            prefix_sum += current.val
            current.next = prefix_sums[prefix_sum].next
            current = current.next
        return front.next
  
  
  
########################################## Memory friendly solution added ##########################################


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            # Add current's value to the prefix sum
            prefix_sum += current.val

            # If prefix_sum is already in the hashmap,
            # we have found a zero-sum sequence:
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next

                # Delete zero sum nodes from hashmap
                # to prevent incorrect deletions from linked list
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p += current.val

                # Make connection from the node before 
                # the zero sum sequence to the node after
                prev.next = current.next
            else:
                # Add new prefix_sum to hashmap
                prefix_sum_to_node[prefix_sum] = current

            # Progress to next element in list
            current = current.next

        return front.next