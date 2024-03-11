from itertools import groupby
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=["".join(sorted(i)) for i in strs]
        a=(list(enumerate(a)))
        a.sort(key=lambda x:x[1])
        l=[list(j) for i,j in groupby(a,key=lambda x:x[1])]
        result=[]
        for i in l:
            f=[]
            for j in i:
                new=j[0]
                f.append(strs[new])
            result.append(f)
        return result
    
    
    
################################################################

f = open('user.out', 'w')


for strs in map(loads, stdin):
    w = defaultdict(list)
    for s in strs:
        w[''.join(sorted(s))].append(s)
    
    print(str(w.values())[12:-1].replace("'", '"').replace(" ", ""), file=f)
exit()