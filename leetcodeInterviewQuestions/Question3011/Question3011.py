class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax, currMin, currMax=0, 0, 0
        prevBit=-1
        for  x in nums:
            b=x.bit_count()
            if prevBit!=b:
                if currMin<prevMax: return False
                prevMax=currMax
                currMin, currMax=x, x
                prevBit=b
            else:
                currMin=min(currMin, x)
                currMax=max(currMax, x)
        return currMin>=prevMax
        