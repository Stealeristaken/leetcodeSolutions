class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        arr=[0]*24
        maxi=1
        for i in range(24):
            for j in range(len(candidates)):
                if candidates[j] & (1 << i):
                    arr[i]+=1
            maxi=max(maxi,arr[i])
        print(arr)
        return maxi