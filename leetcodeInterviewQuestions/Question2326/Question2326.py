# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix=[[-1]*n for i in range(m)]
        top=0
        bottom=m-1
        left=0
        right=n-1
        while top<=bottom and left<=right and head:
            #top row
            for i in range(left,right+1):
                if head:
                    matrix[top][i]=head.val
                    head=head.next
                else:
                    return matrix
            top+=1
            #right column
            for i in range(top,bottom+1):
                if head:
                    matrix[i][right]=head.val
                    head=head.next
                else:
                    return matrix
            right-=1
            #bottom row
            if top<=bottom and left<=right:
                for i in range(right,left-1,-1):
                    if head:
                        matrix[bottom][i]=head.val
                        head=head.next
                    else:
                        return matrix
                bottom-=1
            if top<=bottom and left<=right:
                for i in range(bottom,top-1,-1):
                    if head:
                        matrix[i][left]=head.val
                        head=head.next
                    else:
                        return matrix
                left+=1
        return matrix
                