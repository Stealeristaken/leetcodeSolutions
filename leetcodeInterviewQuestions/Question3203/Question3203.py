from typing import List
from math import ceil
from collections import defaultdict

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1)
        m = len(edges2)

        # Step 1: Graph formation
        def graph_formation(graph, adj):
            for n1, n2 in graph:
                adj[n1].append(n2)
                adj[n2].append(n1)
            return adj

        adj1 = graph_formation(edges1, defaultdict(list))
        adj2 = graph_formation(edges2, defaultdict(list))

        # Step 2: Find diameter of a graph
        def find_diameter(node, graph):
            max_distance = 0
            farthest_node = 0

            def dfs(curr, parent, distance):
                nonlocal max_distance, farthest_node

                if distance > max_distance:
                    max_distance = distance
                    farthest_node = curr

                for nei in graph[curr]:
                    if nei != parent:
                        dfs(nei, curr, distance + 1)

            dfs(node, -1, 0)
            return max_distance, farthest_node

        # Find diameter of tree 1
        _, farthest1 = find_diameter(0, adj1)
        d1, _ = find_diameter(farthest1, adj1)

        # Find diameter of tree 2
        _, farthest2 = find_diameter(0, adj2)
        d2, _ = find_diameter(farthest2, adj2)

        # Calculate the minimum diameter after merging
        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))