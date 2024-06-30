from collections import defaultdict
class Solution:
    def is_not_connected(self, graph, n):
        def dfs(node, visited):
            visited[node] = True
            for neighbor, _, _ in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)
        if not graph:
            return False
        start_node = list(graph.keys())[0]
        visited = {node: False for node in graph}
        dfs(start_node, visited)
        return False in [visited[v] for v in visited] or len(visited) < n
    
    def prims(self, graph):
        minHeap = []
        for neighbor, weight, tpe in graph[1]:
            heappush(minHeap, [weight, 1, neighbor, tpe])
        mst = []
        visit = set()
        visit.add(1)
        while minHeap:
            weight, src, node, tpe = heappop(minHeap)
            if node in visit:
                continue
            mst.append((tpe, src, node))
            visit.add(node)
            for n, w, t in graph[node]:
                if n not in visit:
                    heappush(minHeap, [w, node, n, t])
        return mst
    
    def check_mst(self, mst):
        out = []
        for node in mst:
            if node in self.edge_set:
                out.append(node)
            elif (node[0], node[2], node[1]) in self.edge_set:
                out.append((node[0], node[2], node[1]))
        return out

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.edge_set = set([tuple(e) for e in edges])
        alice_graph = defaultdict(list)
        bob_graph = defaultdict(list)
        total_edges = len(edges)
        # default weight = 1
        for t,u,v in edges:
            if t == 1:
                alice_graph[u].append((v, 1, t))
                alice_graph[v].append((u, 1, t))
            elif t == 2:
                bob_graph[u].append((v, 1, t))
                bob_graph[v].append((u, 1, t))
            else:
                alice_graph[u].append((v, 0, t))
                alice_graph[v].append((u, 0, t))
                bob_graph[u].append((v, 0, t))
                bob_graph[v].append((u, 0, t))

        
        if self.is_not_connected(alice_graph, n):
            return -1
        
        if self.is_not_connected(bob_graph, n):
            return -1
        
        total_edge = []
        # alice mst
        alice_mst = self.check_mst(self.prims(alice_graph))

        print(f'alice {alice_mst}')
        # bob mst
        bob_mst = self.check_mst(self.prims(bob_graph))
        print(f'bob {bob_mst}')

        if not alice_mst or not bob_mst:
            return -1

        total_edge += alice_mst + bob_mst
        total_edge = set(total_edge)

        return abs(total_edges - len(total_edge))