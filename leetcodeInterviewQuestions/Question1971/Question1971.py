from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        travelled = [0] * n
        source_graph = [source]
        arr = [[] for _ in range(n)]
        for x, y in edges:
            arr[x].append(y)
            arr[y].append(x)
        while source_graph:
            child = []
            for x in source_graph:
                travelled[x] += 1
                if travelled[x] > 1:
                    continue
                if x == destination:
                    return True
                for y in arr[x]:
                    child.append(y)
            source_graph = child
        return False