class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        cumulative_sum = 0
        count = 0 
        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k            
            if remainder < 0:
                remainder += k            
            count += remainder_count[remainder]            
            remainder_count[remainder] += 1
        return count