class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(ind,target):
            if target==0:
                ans.append(op[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    breakw
                op.append(candidates[i])
                solve(i+1,target-candidates[i])
                op.pop()

        candidates.sort()
        ans=[]
        op=[]
        solve(0,target)
        return ans