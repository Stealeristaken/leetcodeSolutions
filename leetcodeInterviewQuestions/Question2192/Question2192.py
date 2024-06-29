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