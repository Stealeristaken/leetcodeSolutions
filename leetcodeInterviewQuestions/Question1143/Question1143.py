class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        lst=[[0 for i in range(len(t1)+1)] for j in range(len(t2)+1)]
        for i in range(1,len(t2)+1):
            for j in range(1,len(t1)+1):
                if t1[j-1]==t2[i-1]:
                    lst[i][j]=1+lst[i-1][j-1]
                else:
                    lst[i][j]=max(lst[i-1][j],lst[i][j-1])
        return lst[-1][-1]
        
        