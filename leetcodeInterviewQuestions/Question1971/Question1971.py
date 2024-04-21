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
  
#####################
  
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if [source, destination] in edges:
            return True
        if source == destination:
            return True
        if n <= 1:
            return True

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = {source}

        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False
        
        return dfs(source)