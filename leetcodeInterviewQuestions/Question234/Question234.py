# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first=ListNode()
        cur=first
        temp=head
        while temp:
            cur.next=ListNode(temp.val)
            temp=temp.next 
            cur=cur.next 
        
        temp=head
        prev=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next

        temp1=prev
        temp2=first.next
        while temp1:
            if temp1.val==temp2.val:
                temp1=temp1.next
                temp2=temp2.next
            else:
                return False
        return True
        
############################################################################################################################################################################




import sys

with open('user.out', 'w') as f:
    while True:
        line = sys.stdin.readline().strip()[1:-1]
        if not line:
            break
        f.write('true\n' if line == line[::-1] else 'false\n')

exit(0)

        
        