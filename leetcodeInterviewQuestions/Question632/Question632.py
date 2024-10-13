from heapq import heappush, heappop, heapify

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        

        minHeap = []
        highest = -math.inf
        for row, li in enumerate(nums):
            packet = [li[0],row,0]
            heappush(minHeap,packet)
            highest = max(highest,li[0])            
        
        
        result = [-10000000,10000000]
        while minHeap:

            lowest, row_index, col_index = heappop(minHeap)
            
            if (result[1] - result[0]) > (highest - lowest):
                result = [lowest,highest]
            col_index +=1
            if col_index < len(nums[row_index]):
                packet = [nums[row_index][col_index],row_index,col_index]
                heappush(minHeap,packet)
                highest = max(highest,nums[row_index][col_index])
            else:
                break

        return result  