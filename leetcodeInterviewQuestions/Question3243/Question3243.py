class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def findMinDistance(node: int, l: int):
            minDistances[node] = min(minDistances[node], l)
            if node == n - 1:
                return
            for v in adj[node]:
                if minDistances[v] <= l + 1: continue
                findMinDistance(v, l + 1)
        adj = [[i + 1] for i in range(n)]
        minDistances = [i for i in range(n)]
        result = []
        for q in queries:
            n1, n2 = q
            adj[n1].append(n2)
            findMinDistance(n1, minDistances[n1])
            result.append(minDistances[-1])
        return result