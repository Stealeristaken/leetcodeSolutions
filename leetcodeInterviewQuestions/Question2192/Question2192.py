class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        lst=[]
        def search(node,mem):
            lst=[]
            if node in mem:
                lst.extend(mem[node])      
            else:
                for edge in edges:
                    if edge[1]==node:
                        lst.append(edge[0])
                        lst1,mem=search(edge[0],mem)
                        lst.extend(lst1)
            mem[node]=list(set(lst))
            # lst=list(set(lst))
            # lst.sort()
            return lst,mem
        for i in range(n):
            lst.append([])
        m={}
        for edge in edges:
            lst[edge[1]],m=search(edge[1],m)
        for i in range(n):
            temp=list(set(lst[i]))
            temp.sort()
            lst[i]=temp
        return lst
  
  
  
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        incoming=defaultdict(list)
        for s,d in edges:
            incoming[d].append(s)
        def bfs(index,incoming_array):
            queue=deque()
            array=set()
            visited=set()
            for i in incoming_array:
                queue.append(i)
                array.add(i)
                visited.add(i)
            while queue:
                ele=queue.popleft()
                for neigh in incoming[ele]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
                        array.add(neigh)
            return sorted(array)
        for i in range(n):
            if incoming[i]:
                ans[i] = bfs(i,incoming[i])
        
        return ans
