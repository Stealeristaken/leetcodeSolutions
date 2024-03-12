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