class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        result = 0
        freq_map = defaultdict(int)
        
        for right in range(len(nums)):
            freq_map[nums[right]] += 1
            
            while max(freq_map.keys()) - min(freq_map.keys()) > 2:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1
            
            result += (right - left + 1)
        
        return result


