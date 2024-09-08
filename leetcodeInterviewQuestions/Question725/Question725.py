class Solution(object):
    def splitListToParts(self, root, k):
        # Count the length of the linked list
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        len_head = 0
        curr = head
        while curr:
            len_head += 1
            curr = curr.next
        elements_in_k = len_head//k
        additional_elements = len_head%k
        number_elements_k = []
        for i in range(k):
            if additional_elements:
                number_elements_k.append(elements_in_k+1)
                additional_elements -= 1
            else:
                number_elements_k.append(elements_in_k)
        curr = head
        idx = 0
        len_curr = 0
        k_linked_lists = []
        while curr:
            len_curr += 1
            if len_curr == number_elements_k[idx]:
                next_head = curr.next
                curr.next = None
                k_linked_lists.append(head)
                head = next_head
                curr = head
                idx += 1
                len_curr = 0
                continue
            curr = curr.next
        number_zeros = number_elements_k.count(0)
        while number_zeros:
            k_linked_lists.append(None)
            number_zeros -= 1
        return k_linked_lists