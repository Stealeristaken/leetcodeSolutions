class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(path,num):
            if not num:
                res.append(path)
                return
            for i in range(len(num)):
                dfs(path + [num[i]], num[:i] + num[i + 1:])

        dfs([],nums)
        return res