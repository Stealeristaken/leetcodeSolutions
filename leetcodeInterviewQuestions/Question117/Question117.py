"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        q = deque([(root,0)])
        curlevel = 0
        prev = Node()
        while q:
            curnode,level = q.popleft()
            if not curnode:
                continue
            
            if level != curlevel:
                prev = curnode
                curlevel += 1
            else:
                prev.next = curnode
                prev = prev.next

            q.append((curnode.left,level+1))
            q.append((curnode.right,level+1))

        return root
        