class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans  = 0
        start = 0
        max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans
  
  
  
  
  
########### Another Solution ###########  


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = nums[0]
        ps = [0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > ma:
                ma = nums[i]
                ps = [i]
            elif nums[i] == ma:
                ps.append(i)
        if len(ps) < k:
            return 0
        ans = 0
        idx = -1
        for l in range(len(ps)-k+1):
            ans += (n - ps[l+k-1]) * (ps[l] - idx)
            idx = ps[l]
        return ans
