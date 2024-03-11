class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        check = (1 << n) - 1
        res = float('inf')
        for i in range(n):
            queue = [(i, 1 << i)]
            distance = [[float('inf') for _ in range(1 << n)] for _ in range(n)]
            distance[i][1 << i] = 0

            while (len(queue) > 0):
                fr = queue[0]
                queue.pop(0)

                node = fr[0]
                mask = fr[1]

                if mask == check:
                    res = min(res, distance[node][mask])
                    break

                for nei in graph[node]:
                    new_mask = mask | (1 << nei)
                    if (distance[nei][new_mask] > distance[node][mask] + 1):
                        distance[nei][new_mask] = distance[node][mask] + 1
                        queue.append((nei, new_mask))
        return res