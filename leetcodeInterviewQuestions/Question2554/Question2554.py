class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        nums_used = 0
        accumulated_sum = 0
        for i in range(1,n+1):
            if i not in banned:
                if accumulated_sum+i <= maxSum:
                    accumulated_sum+=i
                    nums_used+=1
                else:
                    break
        return     nums_used    


        