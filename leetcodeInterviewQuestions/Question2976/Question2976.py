class Solution:

    def dijkstra(self, start, end , graph, char_set):
        if start == end:
            return 0
        pq = [(0, start)]
        distances = {char: float('inf') for char in char_set}
        distances[start]=0
        while pq:
            current_cost, current_char = heapq.heappop(pq)
            if current_cost > distances[current_char]:
                continue
            if current_char not in graph:
                return -1
            for neighbor, weight in graph[current_char].items():
                distance = current_cost + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        if end not in distances:
            return -1
        return distances[end] if distances[end] != float('inf') else -1
 

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1
        n = len(source)
        char_set = set(original + changed)
        graph = {char: {} for char in char_set}
        for i in range(len(original)):
            if changed[i] in graph[original[i]]:
                graph[original[i]][changed[i]] = min(graph[original[i]][changed[i]], cost[i])
            else:
                graph[original[i]][changed[i]] = cost[i]
       
        total_cost = 0
        cache={}
        for i in range(n):
            if source[i] != target[i]:
            
                if source[i] in cache and target[i] in cache[source[i]]:
                    cost = cache[source[i]][target[i]]
                else:
                    cost = self.dijkstra(source[i], target[i],graph, char_set )
                    cache[source[i]] = cache.get(source[i],{})
                    cache[source[i]][target[i]] = cost
                if cost == -1:
                    return -1
                total_cost += cost
        return total_cost