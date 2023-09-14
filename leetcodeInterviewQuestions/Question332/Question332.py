class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        outdegree = defaultdict(int)

        for a, b in tickets:
            graph[a].append(b)
            outdegree[a] += 1

        for node in graph:
            graph[node].sort(reverse=True)

        stack = ["JFK"]
        ans = deque()

        while stack:
            top = stack[-1]

            if outdegree[top] == 0:
                ans.appendleft(stack.pop())
            else:
                stack.append(graph[top].pop())
                outdegree[top] -= 1

        return ans