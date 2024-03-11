class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        q = [(0, 0), (0, firstPerson)]

        graph = collections.defaultdict(list)
        for person_i, person_ii, time in meetings:
            graph[person_i].append((person_ii, time))
            graph[person_ii].append((person_i, time))

        answer = set()
        while q:
            time, person_i = heapq.heappop(q)
            if person_i in answer:
                continue
            answer.add(person_i)
            for person_ii, meeting_time in graph[person_i]:
                if meeting_time >= time:
                    heapq.heappush(q, (meeting_time, person_ii))
        return list(answer)
  
  
  
  
  
################################################################################################################


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def handle(nodes):
            adj = defaultdict(set)
            n_t_h = set()
            for x, y, _ in nodes:
                if secret[x]:
                    n_t_h.add(x)
                if secret[y]:
                    n_t_h.add(y)
                adj[x].add(y)
                adj[y].add(x)
            
            while n_t_h:
                n_n_t_h = set()
                for node in n_t_h:
                    for neighbor in adj[node]:
                        if secret[neighbor]:
                            continue
                        secret[neighbor] = True
                        n_n_t_h.add(neighbor)
                n_t_h = n_n_t_h
            
            
        meetings.sort(key=lambda e: e[2])
        i = 0
        m = len(meetings)
        secret = [False for i in range(n)]
        secret[0] = True
        secret[firstPerson] = True

        while i < m:
            time = meetings[i][2]
            to_handle = []
            while i < m and meetings[i][2] == time:
                if not secret[meetings[i][0]] or not secret[meetings[i][1]]:
                    to_handle.append(meetings[i])
                i += 1
            handle(to_handle)
        
        return [i for i in range(n) if secret[i]]