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