from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        last_height = 0
        ans = 0

        while left<right:
            if height[left]<height[right]:
                if height[left]>last_height:
                    ans += (height[left]-last_height)*(right-left)
                    last_height = height[left]
                ans -= height[left]
                left+=1
            else:
                if height[right]>last_height:
                    ans += (height[right]-last_height)*(right-left)
                    last_height = height[right]
                ans -= height[right]
                right-=1
        return ans
    
    
    
class Solution:
    def trap(self, height: List[int]) -> int:
        rainwater = 0 
        for i in range(1, len(height)):
            min_height = min( max(height[0:i]), max(height[i:len(height)]))
            if((min_height - height[i]) > 0):
                rainwater += (min_height - height[i])
        return rainwater