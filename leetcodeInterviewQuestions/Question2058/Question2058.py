# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_indexes = []

        prev = ListNode(head.val)
        current = head
        counter = 0
        while current:
            next = current.next
            if not next:
                next = ListNode(current.val)
            
            if (current.val > prev.val and current.val > next.val) or (current.val < prev.val and current.val < next.val):
                # got a critical point
                critical_indexes.append(counter)
            
            prev = current
            current = current.next
            counter +=1
        if len(critical_indexes) < 2:
            return [-1,-1]
        print(critical_indexes)

        minDist = 10**5
        for i in range(0, len(critical_indexes)-1):
            minDist = min(minDist, critical_indexes[i+1] - critical_indexes[i])
        

        return [minDist,critical_indexes[-1] - critical_indexes[0]]
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = None
        last = None
        prev_val = None
        idx = 0
        min_dist = float('inf')

        while head.next:
            if prev_val and ((head.val < prev_val and head.val < head.next.val) or (head.val > prev_val and head.val > head.next.val)):
                if first is None:
                    first = idx
                
                if last is not None:
                    min_dist = min(min_dist, idx - last)
                
                last = idx
            
            prev_val = head.val
            idx += 1
            head = head.next

        if first != last:
            return [min_dist, last - first]

        return [-1, -1]