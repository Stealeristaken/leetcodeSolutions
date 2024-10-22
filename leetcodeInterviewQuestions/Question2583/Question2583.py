class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        pq = []

        while queue:
            level = 0

            for _ in range(len(queue)):
                curr = queue.popleft()
                level += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            heapq.heappush(pq,  level)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0] if len(pq) == k else -1